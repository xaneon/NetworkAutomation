from netmiko import ConnectHandler
import credentials as cred

device1 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip,
    'username': cred.username,
    'password': cred.password,
    'port': cred.port,
}

device2 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip2,
    'username': cred.username2,
    'password': cred.password2,
    'port': cred.port2,
}

device3 = {
    'device_type': 'cisco_nxos',
    'ip': cred.ip3,
    'username': cred.username3,
    'password': cred.password3,
    'port': cred.port3,
}


device_list = [device1, device2, device3]

for device in device_list:
    nc = ConnectHandler(**device)
    cmd = "show version"
    output = nc.send_command_expect(cmd)
    print(output, type(output))

    # conf_cmd = ["line vty 0 4", 
    #             "transport input all"]
    # output = nc.send_config_set(conf_cmd)
    # print(output, type(output))
