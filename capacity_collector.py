#!/usr/bin/python3
import urllib3
import datetime
import json
from pypureclient import flasharray

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = flasharray.Client('nnn.nnn.nnn.nnn',
                           version='2.2',
                           private_key_file='/data/rest-key.pem',
                           private_key_password='',
                           username='k8s',
                           client_id='your-client-id',
                           key_id='your-key-id',
                           issuer='who-issued-thi')

myvol = client.get_volumes_space(names=["*"])
# Thought about addding all dicts to a single list, will experiment

for item in myvol.items:
    output = {
        "name": item.name,
        "time": datetime.datetime.fromtimestamp(item.time / 1e3).isoformat(),
        "phys_size": item.space.total_physical
    }

    print(json.dumps(output))
