import json

fname = "demo_json.json"

with open(fname, "r") as fid:
    out = fid.read()

json_dict = json.loads(out)

for k, v in json_dict.items():
    print ("key: {}, value: {} ({})".format(k, v, type(v)))

