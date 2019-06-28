from pysnmp.hlapi import getCmd, nextCmd, SnmpEngine, CommunityData
from pysnmp.hlapi import UdpTransportTarget, ContextData, ObjectType
from pysnmp.hlapi import  ObjectIdentity
import credentials2 as cred

oid = ObjectIdentity('1.3.6.1.2.1.25.2.3.1.3')

target_addr = (cred.ip, cred.snmp_port)

snmp_engine_obj = SnmpEngine()
com_data_obj = CommunityData(cred.community_string)
udp_transport_target_obj = UdpTransportTarget(target_addr)
context_data_obj = ContextData()
otype_oid = ObjectType(oid)

gen = nextCmd(snmp_engine_obj, com_data_obj,
              udp_transport_target_obj,
              context_data_obj, otype_oid,
              lexicographicMode=False)


for *errorInformation, varBinds in gen:

    # errorIndication, errorStatus, errorIndex = errorInformation
    print(errorInformation)  # [None, 0, 0]

    for rfc1902obj in varBinds:
        print(rfc1902obj.prettyPrint())

