import json

from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home')
def home(request):
    # https://docs.pylonsproject.org/projects/pyramid/en/latest/api/request.html
    # Response
    response = request.response
    response.content_type = 'application/json'
    response.status_code = 200
    # body
    set_json_to_responce(response, {'project': 'BackHP'})
    return response


def set_json_to_responce(response, json_data):
    response = response
    response.text = json.dumps(json_data)
    return response
