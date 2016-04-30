# -*- coding: utf-8 -*-

from zope.interface import implements
from scrapyd.interfaces import ISpiderScheduler
from scrapyd import scheduler

from scrapyd_mongodb.utils import get_spider_queues


class SpiderScheduler(scheduler.SpiderScheduler):

    implements(ISpiderScheduler)

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
