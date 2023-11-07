import azure.functions as func
from flask import Flask, jsonify
from flasgger import Swagger

app = func.FunctionApp()
swagger = Swagger(app)

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")

