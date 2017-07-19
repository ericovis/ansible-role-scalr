#!/usr/bin/env python
ENCODING='utf-8'
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("admin_password", help="Admin password for the Scalr server")
args = parser.parse_args()

input_file = '/etc/scalr-server/scalr-server-secrets.json'


with open(input_file) as f:
    output = json.load(f)

output['app']['admin_password'] = args.admin_password

with open(input_file, 'w') as f:
    json.dump(output, f)
