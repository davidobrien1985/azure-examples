import json
import os
import uuid
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

client = authenticate_graph_api()

user = {
  "accountEnabled": True,
  "displayName": "example user",
  "mailNickname": "exampleuser",
  "userPrincipalName": "example@example-domain.net",
  "passwordProfile": {"forceChangePasswordNextSignIn": True, "password": str(uuid.uuid4())}
}

response = client.post("/users", json.dumps(user),headers={'Content-Type': 'application/json'})
print(response.content)