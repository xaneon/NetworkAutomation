#!/usr/bin/python3.6
from lxml import etree as ET

template_fname = "demo_xslt_interfaces_template.xsl"
xml_datafname = "demo_xslt_interfaces.xml"
html_fname = "demo_interfaces.html"

with open(template_fname, "r") as fid:
    out1 = fid.read()

xslRoot = ET.fromstring(out1.encode("utf-8"))
transform = ET.XSLT(xslRoot)

with open(xml_datafname, "r") as fid:
    out2 = fid.read()

xmlRoot = ET.fromstring(out2.encode("utf-8"))
transRoot = transform(xmlRoot)

with open(html_fname, "w") as fid:
    fid.write(ET.tostring(transRoot).decode("utf-8"))

