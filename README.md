
# Scrapyd-mongodb
[![PyPI version](https://badge.fury.io/py/scrapyd-mongodb.svg)](https://badge.fury.io/py/scrapyd-mongodb)

Scrapyd is a fantastic open-source library for management of crawlers using scrapy-framework.
However, the builtin queue management is implemented to work using SQLite which ends up being a problem when we need to scale.

This library is designed to replace the SQLite backend by a MongoDB backend. In other words, all
the queue management will be done using MongoDB.


## Install

You need to have MongoDB installed before using this library. The documentation to install it can be found at: https://docs.mongodb.org/manual/installation/

`scrapyd-mongo` is available at pypi:

```bash

$ pip install scrapyd-mongodb

```

## Config

To start using this library you just need to override the `application` option in your `scrapy.cfg` file:
```cfg

[scrapyd]
application = scrapyd_mongodb.application.get_application
...

```

If you want to customize the access to the database, you can add into your `scrapy.cfg` file:

```cfg
[scrapyd]
mongodb_name = scrapyd_mongodb
mongodb_host = 127.0.0.1
mongodb_port = 27017
mongodb_user = custom_user  # (Optional)
mongodb_pass = custompwd  # (Optional)
...

```


## Contributing

Having trouble? have suggestions?  
Report bugs or suggestions on the issue tracker.
