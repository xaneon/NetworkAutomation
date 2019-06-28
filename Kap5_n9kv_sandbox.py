from netmiko import ConnectHandler
from credentials import username, password, ip
from time import sleep


# Dictionary mit allen Informationen zu Device und Verbindung
n5k1 = {'device_type': 'cisco_nxos',
        'ip': ip,
        'username': username,
        'password': password}

# Verbindungsaufbau über den Konstruktor der Klasse ConnectHandler. Das
# Dictionary wird hier verwendet um seinen Inhalt als Keyword-Arguments zu
# übergeben.
net_connect = ConnectHandler(**n5k1)
print('Connected')
net_connect.send_config_set(['feature nxapi'])
sleep(5)
commands = ['nxapi https port 8443']
net_connect.send_config_set(commands)
print('Done')

# cleanup = ['no feature nxapi',
#            'no nxapi https port 8443',
#            'no nxapi sandbox']
# cleanup.reverse()
# net_connect.send_config_set(cleanup)
# print('Done')
