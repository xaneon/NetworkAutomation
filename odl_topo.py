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
def get_topology(odl_ip=ODL_IP, odl_port=ODP_RESTCONF_PORT):
    # Konstruktion des URL-Strings aus Protokoll, Hostsystem und Resource.
    url_base = 'http://%s:%s' % (odl_ip, odl_port)
    url_resource = '/restconf/operational/network-topology:network-topology'
    url = url_base + url_resource
    # HTTP-GET Request an diese URL unter Verwendung der Oben definierten
    # Login-Daten und Header mit Hilfe von requests. Die Funktion gibt das
    # entsprechende Objekt zurück.
    return requests.get(url, auth=AUTH, headers=HDR)


def list_nodes(topology_response, id='flow:1'):
    topos = json.loads(topology_response.text)["network-topology"]["topology"]
    node_list = []
    for topo in topos:
        if topo['topology-id'] == id:
            node_list.extend(topo['node'])
            # link_list = topo['link']
    return node_list


def list_hosts(node_list):
    return [node for node in node_list if node['node-id'].startswith('host')]


def host_lookup(host_list, ip='', mac=''):
    att_pts = []
    if ip and not mac:
        for node in host_list:
            for add in node["host-tracker-service:addresses"]:
                if add['ip'] == ip:
                    att_pts = node["host-tracker-service:attachment-points"]
    if mac and not ip:
        for node in host_list:
            for add in node["host-tracker-service:addresses"]:
                if add['mac'] == mac:
                    att_pts = node["host-tracker-service:attachment-points"]
    if ip and mac:
        for node in host_list:
            for add in node["host-tracker-service:addresses"]:
                if add['ip'] == ip and add['mac'] == mac:
                    att_pts = node["host-tracker-service:attachment-points"]
    if att_pts:
        tp_id_elements = att_pts[0]['tp-id'].split(':')
        return {'node': ':'.join(tp_id_elements[:-1]),
                'port_id': tp_id_elements[-1]}


def main():
    resp = get_topology()
    # print(resp.text)
    nodes = list_nodes(resp)
    print(nodes)
    hosts = list_hosts(nodes)
    print(hosts)
    # print(host_lookup(hosts, mac='f6:26:38:5c:83:eb'))
    print(host_lookup(hosts, mac='a2:64:e5:32:c1:5b'))
    print(host_lookup(hosts, ip='10.0.0.5'))


if __name__ == '__main__':
    main()
