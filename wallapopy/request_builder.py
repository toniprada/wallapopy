# -*- coding: utf-8 -*-
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlencode

class WallapopRequestBuilder:

    BASE_URL = 'http://pro2.wallapop.com/shnm-portlet/api/v1'

    def user(self, user_id):
        endpoint = 'user.json/%s' % user_id
        return self._build_request('GET', endpoint, {})

    def user_reviews_received(self, user_id):
        endpoint = 'review.json/user/%s/received' % user_id
        return self._build_request('GET', endpoint, {})

    def user_reviews_sent(self, user_id):
        endpoint = 'review.json/user/%s/send' % user_id
        return self._build_request('GET', endpoint, {})

    def user_items_published(self, user_id, start=0, end=250):
        return self._build_items_request('PUBLISHED', user_id, start, end)

    def user_items_sold(self, user_id, start=0, end=250):
        return self._build_items_request('SOLD_OUTSIDE', user_id, start, end)

    def search(self, latitude, longitude, query=None, category_ids=None, order_by='creationDate', order_type='des',
               time_filter='noLimit'):
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'orderBy': order_by,
            'orderType': order_type,
            'timeFilter': time_filter
        }
        if query: params['keywords'] = query
        if category_ids: params['categoryIds'] = category_ids
        return self._build_request('GET', 'item.json/search8', params)

    def _build_items_request(self, items_state, user_id, start, end):
        endpoint = 'item.json/user2/%s' % user_id
        params = {
            'init': start,
            'end': end,
            'statuses': items_state
        }
        return self._build_request('GET', endpoint, params)

    def _build_request(self, method, endpoint, params):
        url = '%s/%s?%s' % (self.BASE_URL, endpoint, urlencode(params))
        return {'method': method, 'url': url}
