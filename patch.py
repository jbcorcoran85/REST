import requests

def patch(service, headers, body):
    #{{_endpoint}}/services/data/v{{version}}/query/?q=select id from namedcredential
    print('PATCH request')
    r = requests.patch(url=service, headers=headers, data=body)
    response = r.json()
    print(response)
    return response