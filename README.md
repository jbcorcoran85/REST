# REST
Salesforce REST API

# Getting started with Postman and Salesforce
https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_rest

https://trailhead.salesforce.com/content/learn/projects/quick-start-connect-postman-to-salesforce

# Salesforce NamedCredential Tooling API
https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_namedcredential.htm?q=named%20credential

# Create Connected App for Auth



# Create Cert for jwt auth
https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm


# REST Auth
https://developer.salesforce.com/docs/atlas.en-us.cgcloud_rtr_dev_guide.meta/cgcloud_rtr_dev_guide/rtr_getting_access_token.htm?_ga=2.181546850.418996376.1692881321-452783423.1689813158

# Connected App w/ server.key auth
https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm&type=5

# Services
## Query
{{_endpoint}}/services/data/v{{version}}/query/?q=select id, developername from namedcredential where developername='test'

## Get
{{_endpoint}}/services/data/v{{version}}/tooling/sobjects/namedcredential/0XADn000000L509



### Lightning Component Bundle
GET:  
{{_endpoint}}/services/data/v{{version}}/tooling/sobjects/lightningcomponentbundle

Query:  
{{_endpoint}}/services/data/v{{version}}/tooling/query/?q=select id from lightningcomponentbundle
