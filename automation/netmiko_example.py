import paramiko_settings
from netmiko import ConnectHandler
import credentials as cred

device1 = {
    'device_type': 'cisco_nxos',
    'ip': "192.168.181.21",
    'username': "admin",
    'password': "cisco",
    'port': "22",
}

device2 = {
    'device_type': 'cisco_nxos',
    'ip': "192.168.181.22",
    'username': "admin",
    'password': "cisco",
    'port': "22",
}

devices = [device1, device2]

for device in devices:

    nc = ConnectHandler(**device)

    cmd = "show version"
    out = nc.send_command_expect(cmd)
    print(out, type(out))

    conf_cmd = ["vlan 890", "name TestVLAN5"]

    out = nc.send_config_set(conf_cmd)
    print(out, type(out))
