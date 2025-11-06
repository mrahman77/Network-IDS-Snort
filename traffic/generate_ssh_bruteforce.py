#!/usr/bin/env python3
"""Simulate SSH brute-force-like SYNs"""
import argparse, time, random
from scapy.all import IP, TCP, send

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--target', required=True)
    p.add_argument('--port', type=int, default=22)
    p.add_argument('--attempts', type=int, default=30)
    p.add_argument('--maxdelay', type=float, default=0.15)
    a = p.parse_args()
    for i in range(a.attempts):
        send(IP(dst=a.target)/TCP(dport=a.port, flags='S', sport=random.randint(1025,65000)), verbose=False)
        time.sleep(random.random()*a.maxdelay)
    print(f"Sent {a.attempts} SYNs to {a.target}:{a.port}")

if __name__ == '__main__':
    main()
