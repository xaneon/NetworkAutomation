from netmiko import ConnectHandler
from credentials import username, password, ip
from time import time

# Dictionary mit allen Informationen zu Device und Verbindung
n9kv = {'device_type': 'cisco_nxos',
        'ip': ip,
        'username': username,
        'password': password}

# Verbindungsaufbau über den Konstruktor der Klasse ConnectHandler. Das
# Dictionary wird hier verwendet um seinen Inhalt als Keyword-Arguments zu
# übergeben.
net_connect = ConnectHandler(**n9kv)
print('Connected @', time())
print(net_connect.send_command('show version'))
output = net_connect.send_command('show int br')
print(output)
print(type(output))
print('Done @', time())
