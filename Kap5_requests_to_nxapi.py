import requests
# from credentials import username, password, ip
import json
from pprint import pprint
username = "admin"
# ip = "10.1.10.21"
ip = "192.168.181.21"
password = "cisco"
# password = "1234Qwer"

url = "http://{}/ins".format(ip)
cred = (username, password)

command = {"ins_api": {"version": "1.0",
                       "type": "cli_show",
                       "chunk": "0",
                       "sid": "1",
                       "input": "sho version",
                       "output_format": "json"
                       }}

HDR = {'Content-type': 'application/json',
       'Accept': 'application/json'}

resp = requests.post(url, headers=HDR, auth=cred, data=json.dumps(command))

resp_payload = resp.text
print(resp.status_code)
print(resp.text)
print(type(resp_payload))
pyobj = json.loads(resp_payload)
print(type(pyobj))
pyobj2 = resp.json()
print(pyobj == pyobj2)
pprint(pyobj)
