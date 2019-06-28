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

    int_filter = """
                 <interfaces xmlns='http://openconfig.net/yang/interfaces'>
                    <interface/>
                 </interfaces>
                 """

    # One particular Vlan, IETF vlan Yang model
    vlans_filter = """
                 <vlans xmlns='http://openconfig.net/yang/vlan'>
                    <vlan>
                        <vlan-id>
                            99
                        </vlan-id>
                    </vlan>
                 </vlans>
                 """

    # All installed Vlans, IETF vlan Yang model
    vlans_filter = """
                 <vlans xmlns='http://openconfig.net/yang/vlan'>
                    <vlan>
                        <vlan-id/>
                    </vlan>
                 </vlans>
                 """

    # Native Yang model Cisco
    cisco_native = """
                   <System xmlns='http://cisco.com/ns/yang/cisco-nx-os-device'>
                        <bd-items>
                            <bd-items>
                                <BD-list>
                                    <fabEncap/>
                                </BD-list>
                            </bd-items>
                        </bd-items>
                   </System>
                   """
    # evtl. later useful
    # :m1="http://www.cisco.com/nxos:7.0.3.I7.3.:configure__vlan"

    ints = cisco_manager.get_config(source="running", filter=('subtree', int_filter))
    # ints = cisco_manager.get_config(source="running", filter=('subtree', cisco_native))
    # vlans = cisco_manager.get_config(source="running", filter=('subtree', vlans_filter))
    # native = cisco_manager.get_config(source="running", filter=('subtree',
    #                                   cisco_native))

    # print(vlans)
    # print(native)
    # print(type(ints))

    print(ints)


