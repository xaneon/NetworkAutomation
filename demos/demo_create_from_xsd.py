import os
xsd_fname = "demo_xsd.xsd"
python_mname = "demo_xsd"
out_fname = "demo_xsd_created_with_script.xml"
os.system(f"pyxbgen -u {xsd_fname} -m {python_mname}")
import demo_xsd
dev = demo_xsd.device()
type(dev)
dev.vendor = "Cisco"
dev.model = "Nexus"
dev.osver = "6.1"
out = dev.toxml("utf-8").decode("utf-8")
with open(out_fname, "w") as fid:
    fid.write(out)
