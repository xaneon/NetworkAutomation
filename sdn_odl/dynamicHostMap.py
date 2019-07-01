from Kap5_SDN_odl_vtn import *
from Kap5_SDN_odl_topo import *
from pprint import pprint
import json

ten = 'vtn1'
br = 'vbr1'

create_tenant(ten)
create_vbridge(ten, br)
create_vinterface(ten, br, 'if1')
create_vinterface(ten, br, 'if2')
r = list_tenants()
pprint(json.loads(r.text))

resp = get_topology()
nodes = list_nodes(resp)
hosts = list_hosts(nodes)
h1_att_pt = host_lookup(hosts, ip='10.0.0.5')
h2_att_pt = host_lookup(hosts, ip='10.0.0.1')
print(h1_att_pt)
print(h2_att_pt)

set_portmap(ten, br, 'if1', node=h1_att_pt['node'],
            port_id=h1_att_pt['port_id'], verbose=True)
set_portmap(ten, br, 'if2', node=h2_att_pt['node'],
            port_id=h2_att_pt['port_id'], verbose=True)

r = list_tenants()
pprint(json.loads(r.text))
