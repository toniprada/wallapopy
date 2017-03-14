# wallapopy

This library provides a pure Python client for Wallapop. It works with Python versions from 2.6+ and Python 3.

## API

Already implemented:

* User:
    * Profile.
    * Sold items.
    * Unsold published items.
    * Reviews sent to others.
    * Reviews received by others.
* Items search.

Other endpoints will be implemented as needed or requested.

## Installing

You can install wallapopy using:

```
$ pip install wallapopy
```

## Using

The motivation for this project was to enable research about reputation in the Sharing Economy. Because I needed lots of data, it includes not only a _client_ but also a _request builder_ which can be used together with Scrapy [(example)](https://github.com/toniprada/wallapop-users-scraper).

### Client

```python
>>> from wallapopy import WallapopClient
>>> client = WallapopClient()
>>> client.user(40000000)
{u'gender': u'M', u'image': {u'averageHexColor': u'565b51', u'pictureId': 148033140...
```

### Request Builder

It returns how to query the data: at the moment the url and HTTP method as nothing more is needed for the implemented endpoints.

```python
>>> from wallapopy import WallapopRequestBuilder
>>> request_builder = WallapopRequestBuilder()
>>> request_builder.user(40000000)
{'method': 'GET', 'url': 'http://pro2.wallapop.com/shnm-portlet/api/v1/user.json/40000000?'}
```
