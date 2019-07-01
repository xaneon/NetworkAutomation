import requests

resp = requests.get('http://linuxcommand.org')
print(resp.status_code)
page = open('page.html', 'w')
page.write(resp.text)
