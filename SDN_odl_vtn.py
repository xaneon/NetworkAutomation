# Funktionen zur Bedienung der Opendaylight (ODL) App Virtual Tenant Manager
# Bitte beachten sie, dass diese einen entsprechend konfigurierten Controller
# samt Topologie zur Funktion benötigen, und ausschließlich zu Demonstrations-
# zwecken gedacht sind.

import requests
import json

# Konstanten die im Folgenden häufig verwendet werden
AUTH = ('admin', 'admin')                   # Login-Daten für den ODL
HDR = {'Content-type': 'application/json'}  # http-Header die JSON anfordern
ODL_IP = 'localhost'                         # ODL-IP
ODP_RESTCONF_PORT = '8181'                  # ODL-Port


# Auflistung aller Tenants. Akzeptiert als optionale Argumente ODL-IP und
# ODL-Port. Ohne entsprechende Angabe werden die Oben definierten Default-Werte
# verwendet
def list_tenants(odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT):
    # Konstruktion des URL-Strings aus Protokoll, Hostsystem und Resource.
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operational/vtn:vtns'
    url = url_base + url_resource
    # HTTP-GET Request an diese URL unter Verwendung der Oben definierten
    # Login-Daten und Header mit Hilfe von requests. Die Funktion gibt das
    # entsprechende Objekt zurück.
    return requests.get(url, auth=AUTH, headers=HDR)


def create_tenant(name, odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT):
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operations/vtn:update-vtn'
    url = url_base + url_resource
    data = json.dumps({"input": {"tenant-name": str(name),
                                 "update-mode": "CREATE",
                                 "operation": "SET",
                                 "description": "creating vtn",
                                 "idle-timeout": 300,
                                 "hard-timeout": 0}})
    return requests.post(url, data=data, auth=AUTH, headers=HDR)


def remove_tenant(name, odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT):
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operations/vtn:remove-vtn'
    url = url_base + url_resource
    data = json.dumps({"input": {"tenant-name": str(name)}})
    return requests.post(url, data=data, auth=AUTH, headers=HDR)


def create_vbridge(tenant, name, odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT):
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operations/vtn-vbridge:update-vbridge'
    url = url_base + url_resource
    data = json.dumps({"input": {"tenant-name": str(tenant),
                                 "bridge-name": str(name)}})
    return requests.post(url, data=data, auth=AUTH, headers=HDR)


def create_vinterface(tenant, vbr, ifname, odl_ip=ODL_IP,
                      odl_port=ODP_RESTCONF_PORT):
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operations/vtn-vinterface:update-vinterface'
    url = url_base + url_resource
    data = json.dumps({"input": {"tenant-name": str(tenant),
                                 "bridge-name": str(vbr),
                                 "interface-name": str(ifname)}})
    return requests.post(url, data=data, auth=AUTH, headers=HDR)


def set_portmap(tenant, vbr, ifname, node='', port_name='', port_id='',
                odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT, verbose=False):
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operations/vtn-port-map:set-port-map'
    url = url_base + url_resource
    data_dict = {"input": {"tenant-name": str(tenant),
                           "bridge-name": str(vbr),
                           "interface-name": str(ifname)}}
    if node:
        data_dict["input"]["node"] = str(node)
    if port_name:
        data_dict["input"]["port-name"] = str(port_name)
    if port_id:
        data_dict["input"]["port-id"] = str(port_id)
    data = json.dumps(data_dict)
    if verbose:
        print(data)
    return requests.post(url, data=data, auth=AUTH, headers=HDR)
