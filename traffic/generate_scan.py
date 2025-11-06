#!/usr/bin/env python3
"""Generate benign SYN scan using Scapy"""
import argparse, time
from scapy.all import IP, TCP, send

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--target', required=True)
    p.add_argument('--ports', default='22,80,443')
    p.add_argument('--delay', type=float, default=0.05)
    a = p.parse_args()
    ports = [int(x) for x in a.ports.split(',') if x.strip()]
    for d in ports:
        send(IP(dst=a.target)/TCP(dport=d, flags='S'), verbose=False)
        time.sleep(a.delay)
    print(f"Sent SYNs to {len(ports)} ports on {a.target}")

if __name__ == '__main__':
    main()
