#! /usr/bin/env python

import unittest
import lxml.etree as et
from ncclient import manager
from ncclient.operations import RPCError

payload = '''
<get-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <source>
      <running/>
    </source>
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <ospf>
              <process-id>
                <id>1</id>
              </process-id>
            </ospf>
          </router-ospf>
        </router>
      </native>
    </filter>
</get-config>
'''

# Connect to the device
with manager.connect(host='10.3.11.1',
                     port=830,
                     username='admin',
                     password='admin',
                     timeout=90,
                     hostkey_verify=False,
                     device_params={'name': 'csr'}) as m:
    try:
        # Execute the get-config RPC
        response = m.dispatch(et.fromstring(payload))
        data = response.xml

        # Convert the response to a string for comparison
        output = et.tostring(et.fromstring(data.encode('utf-8')),pretty_print=True).decode()

        # Define the expected output
        expected_output = '''
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
        '''

        assert expected_output.replace(" ","").replace("\n","") in output.replace(" ", "").replace("\n","")

    except RPCError as e:
        print(f"Test failed (RPCError) {e}")
        exit(1)
    except Exception as e:
        print(f"Test failed {e}")
        exit(1)

    print("Test passed.")
