
# Scrapyd-mongodb

The scrapyd library is a fantastic open-source tool for management of spiders implemented using scrapy-framework.
However, the builtin backend queue management library is implemented to work with SQLite,
which ends up being a problem when we need to scale.

This library is designed to replace the SQLite backend for MongoDB backend. In other words, all
queue management will be done using MongoDB with the help of pymongo library.


## Install

To use this library you need to have installed mongodb on the machine.
The documentation can be found at: https://docs.mongodb.org/manual/installation/

The `scrapyd-mongo` library is available at pypi:

```bash

$ pip install scrapyd-mongodb

```

## Config

The configuration to use this library in your scrapy project is pretty simple.
You just need to override the `application` in your `scrapy.cfg` file:

```cfg

[scrapyd]
application = scrapyd_mongodb.application.get_application
...

```

If you want to customize the info to access the mongodb, you can add into your `scrapy.cfg` file:

```cfg
[scrapyd]
mongodb_name = scrapyd_mongodb
mongodb_host = 127.0.0.1
mongodb_port = 27017
...

```


## Contributing

Having trouble? have suggestions?  
Report bugs or suggestions on the issue tracker.
