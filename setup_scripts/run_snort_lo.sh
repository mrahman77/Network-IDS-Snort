#!/usr/bin/env bash
# Run Snort on loopback (lo) for testing traffic destined to the sensor itself
set -euo pipefail
sudo pkill snort || true
sudo mkdir -p /var/log/snort
echo "[*] Starting snort on loopback (lo) - console mode"
sudo snort -c /etc/snort/snort.conf -i lo -A console
