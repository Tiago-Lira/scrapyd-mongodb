# -*- coding: utf-8 -*-

from zope.interface import implementer
from scrapyd.interfaces import ISpiderQueue
from scrapyd.spiderqueue import SqliteSpiderQueue

from scrapyd_mongodb.mongodb import MongoDBPriorityQueue


@implementer(ISpiderQueue)
class MongoDBSpiderQueue(SqliteSpiderQueue):

    def __init__(self, config, collection):
        self.q = MongoDBPriorityQueue(config, collection)
