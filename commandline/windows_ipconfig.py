import os
from pprint import pprint
fname = "ipconfig.txt"
searchstr = "IPv4"
# generate the ipconfig file:
os.system(f"ipconfig /all > {fname}")

data = dict()
with open(fname, encoding="latin-1") as fid:
    for line in fid:
        if line[0] != " ":
            if line.strip() and line.strip()[-1] == ":":
                adapter = line.strip()[:-1]
        if searchstr in line:
            ipv4addr = line.strip()[36:].replace("(Bevorzugt)", "")
            data[adapter] = ipv4addr
pprint(data)
