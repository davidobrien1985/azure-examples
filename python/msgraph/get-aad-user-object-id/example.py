import json
import os
from azure.identity import ClientSecretCredential
from msgraphcore import GraphSession

# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret

def authenticate_graph_api():
  graph_credentials = ClientSecretCredential(
      client_id=os.environ["AZURE_CLIENT_ID"],
      client_secret=os.environ["AZURE_CLIENT_SECRET"],
      tenant_id=os.environ["AZURE_TENANT_ID"]
  )

  scopes = ['.default']
  return GraphSession(graph_credentials, scopes)

def get_aaduser_object_id(user_principal_name):
  aad_group = graphrbac_client.get(f"/users?$filter=startswith(userPrincipalName, '{user_principal_name}')").json()
  return aad_group['value'][0]['id']

graphrbac_client = authenticate_graph_api()

object_id = get_aaduser_object_id("david@xirus.com.au")
print(object_id)