#!/usr/bin/python3.6
from lxml import etree as ET

template_fname = "demo_xslt_template.xsl"
xml_datafname = "demo_xslt_xmldata.xml"
html_fname = "demo_xslt_html.html"

with open(template_fname, "r") as fid:
    out = fid.read()

xslRoot = ET.fromstring(out.encode("utf-8"))
transform = ET.XSLT(xslRoot)

with open(xml_datafname, "r") as fid:
    out = fid.read()

xmlRoot = ET.fromstring(out.encode("utf-8"))
transRoot = transform(xmlRoot)

with open(html_fname, "w") as fid:
    fid.write(ET.tostring(transRoot).decode("utf-8"))

