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

device_list = [device1, device2]

for device in device_list:
    nc = ConnectHandler(**device)
    # cmd = "show version"
    cmd = "sh ip route"
    output = nc.send_command_expect(cmd)
    # print(output, type(output))

    conf_cmd = ["feature nxapi",
                "nxapi http port 80"]
                # "nxapi https port 443"
    conf_cmd2 = ["feature netconf"]
    conf_cmd2 = ["feature restconf"]
    output = nc.send_config_set(conf_cmd)
    output = nc.send_config_set(conf_cmd2)
    # print(output, type(output))
