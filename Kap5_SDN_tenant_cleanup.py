from Kap5_SDN_odl_vtn import *
import json

tens = json.loads(list_tenants().text)
for i in tens['vtns']['vtn']:
    remove_tenant(i['name'])
r = list_tenants()
remove_tenant('vtn1')
print(r.text)
