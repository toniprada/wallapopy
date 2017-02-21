# wallapopy

A _Wallapop_ client for Python.

_Wallapop_ is a marketplace for second hand articles with a high user penetration in Spain. It follows the _two-sided_ reputation schema, where both seller and buyer receive a rating as well as an optional comment. User profiles consist of profile data, sold products with their associated feedbacks and products on sale.

This library was created to enable research projects related to reputation in the Sharing Economy (results not published yet).

## Data

Endpoints implemented:

* User:
    * Profile (including user metadata).
    * Published and sold items.
    * Sent and received reviews.

* Search: by location and with optional parameters as query term or sorting strategy.


## Usage

Given that this library was intended to be used together with Scrapy, not only a client is included but also a _request builder_ to easily create _Scrapy Requests_ (or whatever it is needed).

### Request Builder

It returns a url that can be queried to access the data together with the method to do it.

```python
from request_builder import WallapopRequestBuilder

request_builder = WallapopRequestBuilder()
print request_builder.user(40000000)
```
```
> {'method': 'GET', 'url': 'http://pro2.wallapop.com/shnm-portlet/api/v1/user.json/40000000?'}
```

### Client

Leveraging the _request builder_, a client that directly downloads the data.

```python
from client import WallapopClient

client = WallapopClient()
print client.user(40000000)
```
```
> {u'gender': u'M', u'image': {u'averageHexColor': u'565b51', u'pictureId': 148033140, u'originalHeight': 416, u'mediumURL': u'http://cdn.wallapop.com/shnm-portlet/images?pictu...
```



