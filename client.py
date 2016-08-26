class WallapopClient:

    BASE_URL = 'http://pro2.wallapop.com/shnm-portlet/api/v1'

    def __init__(self):
        pass

    def search(self, latitude, longitude):
        print self._build_url('item.json/search8', ('longitude', latitude), ('latitude', longitude))
        # TODO additional params for a effective search
        # TODO do request

    def _build_url(self, endpoint, *params):
        params_string = '&'.join(['='.join([tup[0], str(tup[1])]) for tup in  params])
        # TODO encode params
        return '{0}/{1}?{2}'.format(self.BASE_URL, endpoint, params_string )

