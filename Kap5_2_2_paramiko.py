import paramiko
import paramiko_settings
import time
import credentials as cred

rcp = paramiko.SSHClient()
auto_policy = paramiko.AutoAddPolicy()
rcp.set_missing_host_key_policy(auto_policy)
rcp.connect(cred.ip, port=cred.port,
            username=cred.username,
            password=cred.password,
            look_for_keys=False,
            allow_agent=False)

remote_conn = rcp.invoke_shell()
output = remote_conn.recv(nbytes=2**16)

remote_conn.send("show ip int brief\n")
time.sleep(.5)
output = remote_conn.recv(nbytes=2**16)
# print(type(output.decode("utf-8")))

remote_conn.send("conf t\n")
time.sleep(.5)
output = remote_conn.recv(nbytes=2**16)
print(output.decode("utf-8"), type(output))

remote_conn.send("end\n")
time.sleep(.5)
output = remote_conn.recv(nbytes=2**16)
# print(output.decode("utf-8"), type(output))
