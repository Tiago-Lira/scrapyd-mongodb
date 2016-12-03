# -*- coding: utf-8 -*-

from zope.interface import implementer
from scrapyd.interfaces import IPoller
from scrapyd import poller

from scrapyd_mongodb.utils import get_spider_queues


@implementer(IPoller)
class QueuePoller(poller.QueuePoller):

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
