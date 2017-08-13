# -*- coding: utf-8 -*-

import json
import pymongo
from configparser import NoOptionError


class MongoDBPriorityQueue(object):

    def __init__(self, config, collection):
        database_name = config.get('mongodb_name', 'scrapyd_mongodb')
        database_host = config.get('mongodb_host', 'localhost')
        database_port = config.getint('mongodb_port', 27017)
        database_user = self.get_optional_config(config, 'mongodb_user')
        database_pwd = self.get_optional_config(config, 'mongodb_pass')

        if database_user and database_pwd:
            conn_str = (
                'mongodb://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
            ).format(
                db_user=database_user,
                db_pwd=database_pwd,
                db_host=database_host,
                db_port=database_port,
                db_name=database_name,
            )
            self.conn = pymongo.MongoClient(conn_str)
        else:
            self.conn = pymongo.MongoClient(
                host=database_host,
                port=database_port,
            )

        self.collection = self.conn.get_database(database_name)[collection]

    @staticmethod
    def get_optional_config(config, name):
        try:
            return config.get(name).replace('\'', '').replace('"', '')
        except NoOptionError:
            return None

    def put(self, message, priority=0.0):
        self.collection.insert_one({
            'priority': priority,
            'message': self.encode(message)
        })

    def pop(self):
        first_queue = self.collection.find_one({}, sort=[
            ('priority', pymongo.DESCENDING),
        ])
        message = first_queue['message']
        self.collection.delete_one({'_id': first_queue['_id']})
        return self.decode(message)

    def remove(self, func):
        count = 0
        for queue in self.collection.find():
            if func(self.decode(queue['message'])):
                self.collection.delete_one({'_id': queue['_id']})
                count += 1
        return count

    def clear(self):
        self.collection.drop()

    def __len__(self):
        return self.collection.count()

    def __iter__(self):
        queryset = self.collection.find().sort([
            ('priority', pymongo.DESCENDING),
        ])
        return ((self.decode(obj['message']), obj['priority'])
                for obj in queryset)

    def encode(self, obj):
        return json.dumps(obj)

    def decode(self, text):
        return json.loads(text)
