#!/usr/bin/env bash
# Run Snort on enp0s5 (edit IFACE if needed)
set -euo pipefail
IFACE=${IFACE:-enp0s5}
sudo pkill snort || true
sudo mkdir -p /var/log/snort
echo "[*] Starting snort on interface $IFACE (console mode)"
sudo snort -c /etc/snort/snort.conf -i "$IFACE" -A console
