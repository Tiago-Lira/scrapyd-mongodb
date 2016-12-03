# -*- coding: utf-8 -*-

from zope.interface import implementer
from scrapyd.interfaces import ISpiderScheduler
from scrapyd import scheduler

from scrapyd_mongodb.utils import get_spider_queues


@implementer(ISpiderScheduler)
class SpiderScheduler(scheduler.SpiderScheduler):

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
