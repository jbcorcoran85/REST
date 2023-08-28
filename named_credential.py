import requests
import get

def body(auth):
    test=auth.sf_instance
    service=f"https://{auth.sf_instance}/services/data/v57.0/tooling/sobjects/namedcredential/describe"
    
    headers={
        'Content-Type': 'application/json',
        "Authorization": f"{auth.headers['Authorization']}"
    }

    body= """'{ 
    "attributes": {
        "type": "NamedCredential",
        "url": "/services/data/v58.0/tooling/sobjects/NamedCredential/"
    },
    "FullName": "anothertest",
    "Metadata": {
        "allowMergeFieldsInBody": false,
        "allowMergeFieldsInHeader": false,
        "authProvider": null,
        "authTokenEndpointUrl": null,
        "awsAccessKey": null,
        "awsAccessSecret": null,
        "awsRegion": null,
        "awsService": null,
        "calloutStatus": "Enabled",
        "certificate": null,
        "endpoint": "https://test.salesforce.com",
        "generateAuthorizationHeader": true,
        "jwtAudience": null,
        "jwtFormulaSubject": null,
        "jwtIssuer": null,
        "jwtSigningCertificate": null,
        "jwtTextSubject": null,
        "jwtValidityPeriodSeconds": null,
        "label": "test",
        "namedCredentialParameters": null,
        "namedCredentialType": null,
        "oauthRefreshToken": null,
        "oauthScope": null,
        "oauthToken": null,
        "outboundNetworkConnection": null,
        "password": null,
        "principalType": "Anonymous",
        "protocol": "NoAuthentication",
        "urls": null,
        "username": null
    }
}'"""

    get_response = get.get(service, headers, body)
    print(f'get response {get_response}')


def query(auth):
    headers={
        'Content-Type': 'application/json',
        "Authorization": f"{auth.headers['Authorization']}"
    }
    service=f"https://{auth.sf_instance}//services/data/v57.0/query/?q=select id, developername from namedcredential"
    get_response = get.get(service, headers)
    

def run(auth):
    body(auth)
    #query(auth)