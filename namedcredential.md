# Named Credentials

POST  
{{_endpoint}}/services/data/v{{version}}/tooling/sobjects/namedcredential

body: 
``` 
{
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
}
```

# Auth

Be sure you're logged in to only one Salesforce org in your browser.
In Postman, under Collections, Salesforce Platform APIs should be selected.
Be sure No Environment is selected.
The Authorization tab should be open.
Type should be OAuth 2.0.
Click Get New Access Token.

# curl

```
curl --location 'https://ddn00000avb69mab-dev-ed.develop.my.salesforce.com/services/data/v58.0/tooling/sobjects/namedcredential' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ....7X03waY.a09ylN8W' \
--header 'Cookie: BrowserId=az1WtkFdEe6Kvem2CFeTwA; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1' \
--data '{
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
}'
```