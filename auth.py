import argparse
#import click
import requests
from simple_salesforce import Salesforce


def simple_salesforce_auth():
    sf = Salesforce(username=env.sfdc_username, consumer_key=env.connected_app_id, privatekey_file='jwt/server.key', instance=env.salesforce_url)
    print(sf.headers['Authorization'])


def requests_auth():
    print('requests auth')
    """
    curl https://<instance>.salesforce.com/services/oauth2/token -d "grant_type=password" -d "client_id=myclientid" -d "client_secret=myclientsecret" -d "mylogin@salesforce.com" -d "password=mypassword123456"
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description='What the program does')
    parser.add_argument('-ci', '--connected-app-id', default="3MVG9ux34Ig8G5eoX6TR_kdql8zB6vWl_AfSx9FXy2DOqqJIEnwugQHIjaDVgK48_0WKEpT0w_5eFeq9R.OAe", action='store', dest='connected_app_id')      # option that takes a value
    parser.add_argument('-sfdc-url', '--salesforce-url', default="https://test.salesforce.com", action='store', dest='salesforce_url')      # option that takes a value
    parser.add_argument('-sfdc-user', '--sfdc-username', default="", action='store', dest='sfdc-username')      # option that takes a value

    env = parser.parse_args()
    simple_salesforce_auth()
    requests_auth()