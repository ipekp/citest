#! /usr/bin/env python
import traceback
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = [
'''
<edit-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <target>
    <running/>
  </target>
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
            <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <ospf>
                    <process-id>
                        <id>1</id>
                        <network>
                            <ip>0.0.0.0</ip>
                            <wildcard>0.0.0.0</wildcard>
                            <area>0</area>
                        </network>
                    </process-id>
                </ospf>
            </router-ospf>
        </router>
    </native>
  </config>
</edit-config>
'''
]

with manager.connect(host='10.3.11.1',
                     port=830,
                     username='admin',
                     password='admin',
                     timeout=90,
                     hostkey_verify=False,
                     device_params={'name': 'csr'}) as m:

    # execute netconf operation
    for rpc in payload:
        try:
            response = m.dispatch(et.fromstring(rpc))
            data = response.xml
        except RPCError as e:
            data = e.xml
            pass
        except Exception as e:
            traceback.print_exc()
            exit(1)

        # beautify output
        if et.iselement(data):
            data = et.tostring(data, pretty_print=True).decode()

        try:
            out = et.tostring(
                et.fromstring(data.encode('utf-8')),
                pretty_print=True
            ).decode()
        except Exception as e:
            traceback.print_exc()
            exit(1)

        print(out)
