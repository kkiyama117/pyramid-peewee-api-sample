from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home', renderer='json',
             request_method='GET')
def home(request):
    # https://docs.pylonsproject.org/projects/pyramid/en/latest/api/request.html
    response = request.response
    result = {'project': 'BackHP'}
    response.body = result
    return response
