from Kap5_SDN_odl_vtn2 import *
from pprint import pprint
import json


ten = 'vtn1'
br = 'vbr1'
br2 = 'vbr2'

create_tenant(ten)
create_vbridge(ten, br)
create_vinterface(ten, br, 'if1')
create_vinterface(ten, br, 'if2')

set_portmap(ten, br, 'if1', 'openflow:1', 'sN-eth3')
set_portmap(ten, br, 'if2', 'openflow:5', 'sSE-eth4')

r = list_tenants()
pprint(json.loads(r.text))

create_vbridge(ten, br2)
create_vinterface(ten, br2, 'if1')
create_vinterface(ten, br2, 'if2')
set_portmap(ten, br2, 'if1', 'openflow:3', 'sNE-eth5')
set_portmap(ten, br2, 'if2', 'openflow:4', 'sSW-eth4')

r = list_tenants()
pprint(json.loads(r.text))

# remove_tenant(ten)
