import json

#AUTH
credsfile = "../credentials/creds.json"
with open(credsfile) as data_file:
    creds = json.load(data_file)

