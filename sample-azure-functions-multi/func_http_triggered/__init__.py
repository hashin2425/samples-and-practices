""" https://*************.azurewebsites.net/api/func_return_html
"""
import json

from func_http_triggered.something_module import say_hello
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        print(req)

        body = {"message": say_hello()}

        return func.HttpResponse(body=json.dumps(body), status_code=200, mimetype="application/json")
    except Exception as e:  # pylint: disable=broad-except
        return func.HttpResponse(f"Something went wrong: {e}", status_code=400)
