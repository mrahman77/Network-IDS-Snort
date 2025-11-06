#!/usr/bin/env python3
import re, csv, argparse, sys
from datetime import datetime

LINE_RE = re.compile(r'^(?P<ts>\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+).*?\[(?P<gid>\d+):(?P<sid>\d+):(?P<rev>\d+)\]\s+(?P<msg>.+?)\s+\[\*\*\]\s+\[Priority:\s*(?P<prio>\d+)\]\s+\{(?P<proto>[A-Z]+)\}\s+(?P<src>[^\s]+)\s+->\s+(?P<dst>[^\s]+)')

def parse_line(line):
    m = LINE_RE.search(line)
    if not m:
        return None
    d = m.groupdict()
    now = datetime.now()
    mm, dd = map(int, d['ts'].split('-')[0].split('/'))
    time_part = d['ts'].split('-')[1]
    ts_iso = f"{now.year:04d}-{mm:02d}-{dd:02d}T{time_part}"
    return {'timestamp': ts_iso,'gid': d['gid'],'sid': d['sid'],'rev': d['rev'],
            'priority': d['prio'],'message': d['msg'],'protocol': d['proto'],
            'src': d['src'],'dst': d['dst']}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    rows = []
    with open(args.input, 'r', errors='ignore') as f:
        for line in f:
            r = parse_line(line.strip())
            if r:
                rows.append(r)
    if not rows:
        print("No alerts parsed. Check file path or Snort output format.", file=sys.stderr)
    with open(args.output, 'w', newline='') as out:
        w = csv.DictWriter(out, fieldnames=['timestamp','priority','message','protocol','src','dst','gid','sid','rev'])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"Wrote {len(rows)} alerts to {args.output}")

if __name__ == '__main__':
    main()
