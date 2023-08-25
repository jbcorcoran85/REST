import requests

def body(auth_header):
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', params=payload)

def run(auth_header):
    body(auth_header)