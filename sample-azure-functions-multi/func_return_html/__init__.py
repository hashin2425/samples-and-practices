""" https://*************.azurewebsites.net/api/func_return_html
"""

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        print(req)

        # load html template
        with open("./func_return_html/template.html", "r", encoding="utf-8") as file:
            html_template = file.read()

        # render html
        html_content = html_template.format(something_message="Hello world")

        return func.HttpResponse(html_content, status_code=200, mimetype="text/html")
    except Exception as e:  # pylint: disable=broad-except
        return func.HttpResponse(f"Something went wrong: {e}", status_code=400)
