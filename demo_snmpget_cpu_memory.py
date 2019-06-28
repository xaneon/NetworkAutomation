from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData
from pysnmp.hlapi import UdpTransportTarget, ContextData, ObjectType
from pysnmp.hlapi import  ObjectIdentity
import credentials2 as cred

# oid = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
# oid = ObjectIdentity('UCD-SNMP-MIB', 'memAvailReal', 0)
# oid = ObjectIdentity('UCD-SNMP-MIB', 'memTotalReal', 0)
# oid = ObjectIdentity('UCD-SNMP-MIB', 'ssCpuRawIdle', 0)
# oid = ObjectIdentity('SNMPv2-MIB', 'sysName', 0)
# oid = ObjectIdentity('DISMAN-EVENT-MIB', 'sysUpTimeInstance')
# oid = ObjectIdentity('1.3.6.1.2.1.1.9.1.3.1')
# oid = ObjectIdentity('SNMPv2-MIB', 'sysORDescr', 1)
oid = ObjectIdentity('SNMPv2-MIB', 'sysName', 0)

target_addr = (cred.ip, cred.snmp_port)

snmp_engine_obj = SnmpEngine()
com_data_obj = CommunityData(cred.community_string)
udp_transport_target_obj = UdpTransportTarget(target_addr)
context_data_obj = ContextData()
otype_oid = ObjectType(oid)

gen = getCmd(snmp_engine_obj, com_data_obj,
              udp_transport_target_obj,
              context_data_obj, otype_oid)

*errorInformation, varBinds = next(gen)

# errorIndication, errorStatus, errorIndex = errorInformation
print(errorInformation)  # [None, 0, 0]

for rfc1902obj in varBinds:
    print(rfc1902obj.prettyPrint())

