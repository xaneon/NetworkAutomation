from pysnmp.hlapi import setCmd, SnmpEngine, CommunityData
from pysnmp.hlapi import UdpTransportTarget, ContextData, ObjectType
from pysnmp.hlapi import  ObjectIdentity, OctetString
import credentials2 as cred

# MibVariable
oid = ObjectIdentity('SNMPv2-MIB', 'sysName', 0)

target_addr = (cred.ip, cred.snmp_port)

snmp_engine_obj = SnmpEngine()
com_data_obj = CommunityData(cred.community_string)
udp_transport_target_obj = UdpTransportTarget(target_addr)
context_data_obj = ContextData()
# otype_oid = ObjectType(oid, OctetString("New description"))
otype_oid = ObjectType(oid, "New system name")

gen = setCmd(snmp_engine_obj, com_data_obj,
              udp_transport_target_obj,
              context_data_obj,
              otype_oid,
              lookupNames=False, lookupValues=True)

*errorInformation, varBinds = next(gen)
# errorIndication, errorStatus, errorIndex = errorInformation
# print(errorInformation)  # [None, 0, 0]

for rfc1902obj in varBinds:
    print(rfc1902obj.prettyPrint())
