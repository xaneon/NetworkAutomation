#!/usr/bin/env python3
import paramiko_settings
from ncclient import manager
import credentials
from lxml import etree

with manager.connect(host=credentials.ip,
                     port=830, # vorher 22
                     username=credentials.username,
                     password=credentials.password,
                     hostkey_verify=False,
                     device_params={'name': 'nexus'},
                     allow_agent=False,
                     look_for_keys=False
                     ) as cisco_manager:

    run = cisco_manager.get_config(source="running")
    print(run)


