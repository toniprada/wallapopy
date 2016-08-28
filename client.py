import requests
import urllib

class WallapopClient:

    BASE_URL = 'http://pro2.wallapop.com/shnm-portlet/api/v1/'

    def __init__(self, return_urls=False):
      self.return_urls = return_urls

    def user(self, user_id):
      return self._get('user.json/' + str(user_id))

    def user_reviews_received(self, user_id):
      return self._get('review.json/user/' + str(user_id) + '/received')

    def user_reviews_sent(self, user_id):
      return self._get('review.json/user/' + str(user_id) + '/send')

    def user_items_sold(self, user_id, start=0, end=250):
      return self._get_items('SOLD_OUTSIDE', user_id, start, end)

    def user_items_published(self, user_id, start=0, end=250):
      return self._get_items('PUBLISHED', user_id, start, end)

    def search(self, latitude, longitude, query=None, category_ids=None,
      order_by='creationDate', order_type='des', time_filter='noLimit'):
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'orderBy': order_by,
            'orderType': order_type,
            'timeFilter': time_filter
        }
        if query: params['keywords'] = query
        if category_ids: params['categoryIds'] = category_ids
        return self._get('item.json/search8', params)

    def _get_items(self, items_state, user_id, start, end):
      params = {
        'init': start,
        'end': end,
        'statuses': items_state
      }
      return self._get('item.json/user2/' + str(user_id), params)

    def _get(self, endpoint, params=None):
        url = self.BASE_URL + endpoint
        if params: url += '?' + urllib.urlencode(params)
        if self.return_urls:
          return url
        else:
          return requests.get(url).json()
