#!/usr/bin/env python
import yaml
import glob

out = {}
for event in glob.glob("events/*"):
    with open(event, 'r') as h:
        data = yaml.safe_load(h)
        for k, v in data['country'].items():
            if k in out:
                out[k] += v
            else:
                out[k] = v

print(f"code,pop")
for k, v in out.items():
    print(f"{k},{v}")
