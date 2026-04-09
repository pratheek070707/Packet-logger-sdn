# 📡 SDN Packet Logger using POX Controller

## Problem Statement

This project implements a Software Defined Networking (SDN) controller using POX to capture and log packet information in a Mininet network. The controller analyzes incoming packets and identifies protocols such as ARP, ICMP, TCP, and UDP.

---

## Objectives

* Capture packet headers (MAC & IP)
* Identify protocol types (ARP, ICMP, TCP, UDP)
* Log packet details using controller
* Demonstrate SDN controller–switch interaction

---

## Setup Instructions

### 1. Install Dependencies

```bash
sudo apt update
sudo apt install mininet git python3
```

### 2. Clone POX

```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### 3. Add Controller File

Place `packet_logger.py` inside:

```
pox/pox/misc/
```

---

##  Execution Steps

### Step 1: Run Controller

```bash
cd ~/pox
./pox.py misc.packet_logger
```

### Step 2: Run Mininet (new terminal)

```bash
sudo mn -c
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

### Step 3: Test Network

```bash
pingall
```

---

##  Expected Output

### Mininet:

```
*** Results: 0% dropped
```

### POX Controller Logs:

```
Packet: 00:00:00:00:00:01 -> 00:00:00:00:00:02
IP: 10.0.0.1 -> 10.0.0.2
Protocol: ICMP
```

---

##  Testing & Validation

* Ping test using `pingall`
* Protocol detection verified via logs
* Flow behavior observed in controller

---

##  Proof of Execution

Include screenshots of:

* Ping results
* Controller logs
* Flow tables:

```bash
sudo ovs-ofctl dump-flows s1
```

---

##  Concepts Used

* SDN Architecture
* OpenFlow Protocol
* PacketIn Events
* Match-Action Flow Rules

---

##  References

* POX Controller Documentation
* Mininet Documentation
* OpenFlow Switch Specification
