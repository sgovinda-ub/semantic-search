from flask import Flask, jsonify, Response, request
from transformer import Transformer
from loguru import logger

class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response

class FlaskAppWrapper(object):

    def __init__(self, name, **configs):
        self.app = Flask(name)
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)


books = [{'id': 1, 'title': 'Python Essentials', 'author': 'Jane Doe'}]
def querylookup():
    #transformer = Transformer(logger)
    #query = transformer.embed([query_text])
    print(request.query_string)
    return books


