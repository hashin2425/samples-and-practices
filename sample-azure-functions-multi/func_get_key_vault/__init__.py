""" https://*************.azurewebsites.net/api/func_get_key_vault
"""
import azure.functions as func
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        print(req)

        credential = DefaultAzureCredential()

        key_vault_url = "https://***************.vault.azure.net/"
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        secret_name = "******************"
        retrieved_secret = client.get_secret(secret_name)

        return func.HttpResponse(str(retrieved_secret.value), status_code=200)
    except Exception as e:  # pylint: disable=broad-except
        return func.HttpResponse(f"Something went wrong: {e}", status_code=400)
