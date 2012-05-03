import os
import urlparse

from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect

from pod_manager import __version__
from pod_manager.api.urls_v10 import url_map


class API(object):
    def __init__(self):
        self.url_map = url_map

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)

        try:
            endpoint, values = adapter.match()
            return getattr(self, 'handle_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def handle_home(self, request):
        return Response('Pod manager v%s' % (__version__), mimetype='text/plain')

    def handle_list_pods(self, request):
        pass

    def handle_get_pod(self, request):
        pass

    def handle_create_pod(self, request):
        pass
