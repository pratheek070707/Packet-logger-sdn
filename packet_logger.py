from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, arp, icmp, tcp, udp

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        return

    log.info("Packet: %s -> %s", packet.src, packet.dst)

    if packet.type == ethernet.ARP_TYPE:
        log.info("Protocol: ARP")

    elif packet.type == ethernet.IP_TYPE:
        ip = packet.payload
        log.info("IP: %s -> %s", ip.srcip, ip.dstip)

        if isinstance(ip.payload, icmp):
            log.info("Protocol: ICMP")

        elif isinstance(ip.payload, tcp):
            log.info("Protocol: TCP")

        elif isinstance(ip.payload, udp):
            log.info("Protocol: UDP")

    # Forward packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    msg.in_port = event.port
    event.connection.send(msg)


def launch():
    log.info("Packet Logger Running 🚀")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
