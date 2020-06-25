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

def get_aadgroup_object_id(group_display_name):
  aad_group = graphrbac_client.get(f"/groups?$filter=startswith(displayName, '{group_display_name}')").json()
  return aad_group['value'][0]['id']

graphrbac_client = authenticate_graph_api()

object_id = get_aadgroup_object_id("set_to_aad_group_name")
print(object_id)