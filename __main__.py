import argparse
import auth


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description='What the program does')
    parser.add_argument('-ci', '--connected-app-id', default="3MVG9ux34Ig8G5eoX6TR_kdql8zB6vWl_AfSx9FXy2DOqqJIEnwugQHIjaDVgK48_0WKEpT0w_5eFeq9R.OAe", action='store', dest='connected_app_id')      # option that takes a value
    parser.add_argument('-sfdc-url', '--salesforce-url', default="https://test.salesforce.com", action='store', dest='salesforce_url')      # option that takes a value
    parser.add_argument('-sfdc-user', '--sfdc-username', default="jbcorcoran85@gmail.com", action='store', dest='sfdc_username')      # option that takes a value
    parser.add_argument('-key-file', '--key-file', default="jwt/server.key", action='store', dest='keyfile_path')      # option that takes a value

    env = parser.parse_args()
    auth.simple_salesforce_auth(env.sfdc_username, env.connected_app_id, env.salesforce_url, env.keyfile_path)
    auth.requests_auth()
