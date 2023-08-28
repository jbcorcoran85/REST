import requests

def get(service, headers, body):
    #{{_endpoint}}/services/data/v{{version}}/query/?q=select id from namedcredential
    print('Get request')
    r = requests.get(url=service, headers=headers, data=body)
    response = r.json()
    print(response)
    return response