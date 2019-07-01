from lxml import etree as ET

demo_xmlfname = "demo_xslt_interfaces.xml"
root = ET.parse(demo_xmlfname)

print([elem.text for elem in root.iter("name")])
print([elem.text for elem in root.iter("ipv4addr")])


interfaces = root.xpath("interface")
names = root.xpath("interface/name")
ipv4addrs = root.xpath("interface/ipv4addr")

n_interfaces = len(interfaces)
n_names = len(names)
n_ipv4addrs = len(ipv4addrs)
