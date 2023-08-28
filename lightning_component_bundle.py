import requests
import get
import patch

def body(auth):
    test=auth.sf_instance
    service=f"https://{auth.sf_instance}/services/data/v57.0/tooling/sobjects/namedcredential/describe"
    
    headers={
        'Content-Type': 'application/json',
        "Authorization": f"{auth.headers['Authorization']}"
    }

    body= """'{
    "attributes": {
        "type": "LightningComponentBundle",
        "url": "/services/data/v58.0/tooling/sobjects/LightningComponentBundle/0RbDn000004D6aXKAS"
    },
    "Id": "0RbDn000004D6aXKAS",
    "IsDeleted": false,
    "DeveloperName": "myFirstWebComponent",
    "Language": "en_US",
    "MasterLabel": "myFirstWebComponent",
    "NamespacePrefix": null,
    "ManageableState": "unmanaged",
    "CreatedDate": "2023-08-28T02:44:59.000+0000",
    "CreatedById": "005Dn000004bhrnIAA",
    "LastModifiedDate": "2023-08-28T02:44:59.000+0000",
    "LastModifiedById": "005Dn000004bhrnIAA",
    "SystemModstamp": "2023-08-28T02:44:59.000+0000",
    "ApiVersion": 58.0,
    "FullName": "myFirstWebComponent",
    "IsExposed": false,
    "Metadata": {
        "apiVersion": 58.0,
        "capabilities": null,
        "description": null,
        "isExplicitImport": false,
        "isExposed": false,
        "lwcResources": {
            "lwcResource": [
                {
                    "filePath": "lwc/myFirstWebComponent/myFirstWebComponent.js-meta.xml",
                    "source": {
                        "asByteArray": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPExpZ2h0bmluZ0NvbXBvbmVudEJ1bmRsZSB4bWxucz0iaHR0cDovL3NvYXAuc2ZvcmNlLmNvbS8yMDA2LzA0L21ldGFkYXRhIj4KICAgIDxhcGlWZXJzaW9uPjU4LjA8L2FwaVZlcnNpb24+CiAgICA8aXNFeHBvc2VkPmZhbHNlPC9pc0V4cG9zZWQ+CjwvTGlnaHRuaW5nQ29tcG9uZW50QnVuZGxlPg==",
                        "inputStream": {},
                        "length": 208,
                        "maxToKeep": 209
                    }
                },
                {
                    "filePath": "lwc/myFirstWebComponent/myFirstWebComponent.js",
                    "source": {
                        "asByteArray": "aW1wb3J0IHsgTGlnaHRuaW5nRWxlbWVudCB9IGZyb20gJ2x3Yyc7CgpleHBvcnQgZGVmYXVsdCBjbGFzcyBNeUZpcnN0V2ViQ29tcG9uZW50IGV4dGVuZHMgTGlnaHRuaW5nRWxlbWVudCB7fQ==",
                        "inputStream": {},
                        "length": 109,
                        "maxToKeep": 110
                    }
                },
                {
                    "filePath": "lwc/myFirstWebComponent/myFirstWebComponent.html",
                    "source": {
                        "asByteArray": "PHRlbXBsYXRlPgogICAgCjwvdGVtcGxhdGU+",
                        "inputStream": {},
                        "length": 27,
                        "maxToKeep": 28
                    }
                }
            ]
        },
        "masterLabel": "myFirstWebComponent",
        "runtimeNamespace": null,
        "targetConfigs": null,
        "targets": null,
        "urls": null
    },
    "Description": null,
    "TargetConfigs": null,
    "IsExplicitImport": false,
    "RuntimeNamespace": null
}'"""

    get_response = patch.patch(service, headers, body)
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