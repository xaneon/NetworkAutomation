# Parsing und Suchen in simplem xml
# import os
from lxml import etree

# tree = etree.parse(os.path.join('nexus_xml_json_files', 'nexus_int_br.xml'))
tree = etree.parse('nexus_xml_json_files/nexus_int_br.xml')
ifs = tree.findall('outputs')  # vs. find und findall nur auf der akt. Ebene
ifs = tree.find('outputs')
# print(ifs)
ifs = [el for el in tree.iter('intf-name')]  # alle Elemente in beliebiger Tiefe
# print(ifs)
for interface in ifs:
    print(interface.text)

# Was ist der übergeordnete Knoten (Parent)?
# for i in tree.iter('intf-name'):
for i in tree.iter('ROW_intf'):
    # print(i.getparent().tag)
    # print(i.text)
    pre = i.find("prefix")
    infn = i.find("intf-name")
    print(pre.text, infn.text)
