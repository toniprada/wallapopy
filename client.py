import requests

class WallapopClient:

    BASE_URL = 'http://pro2.wallapop.com/shnm-portlet/api/v1/'

    def __init__(self):
        pass

    def search(self, latitude, longitude, order_by='creationDate', order_type='des',
        time_filter='noLimit'):
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'orderBy': order_by,
            'orderType': order_type,
            'timeFilter': time_filter
        }
        return self._get('item.json/search8', params)
        # "&categoryIds=12545%2C12800%2C12579%2C12467%2C12900%2C12463%2C12465%2C12461%2C13000%2C13100%2C12485%2C13200

    def _get(self, endpoint, params):
        r = requests.get(self.BASE_URL + endpoint , params=params)
        print r.url
        return r.json()
