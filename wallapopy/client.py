# -*- coding: utf-8 -*-
import requests
from request_builder import WallapopRequestBuilder

class WallapopClient:

    def __init__(self):
        self.request_builder = WallapopRequestBuilder()

    def __getattr__(self, method_name):
        def client_method(*args, **kwargs):
            request_builder_method = getattr(self.request_builder, method_name)
            request = request_builder_method(*args, **kwargs)
            return self._make_request(request)
        return client_method

    def _make_request(self, request):
        if request['method'] == 'GET':
            return requests.get(request['url']).json()
