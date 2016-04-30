# -*- coding: utf-8 -*-

from zope.interface import implements
from scrapyd.interfaces import ISpiderQueue
from scrapyd.spiderqueue import SqliteSpiderQueue

from scrapyd_mongodb.mongodb import MongoDBPriorityQueue


class MongoDBSpiderQueue(SqliteSpiderQueue):

    implements(ISpiderQueue)

    def __init__(self, config, collection):
        self.q = MongoDBPriorityQueue(config, collection)
