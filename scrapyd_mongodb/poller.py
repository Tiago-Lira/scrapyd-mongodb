# -*- coding: utf-8 -*-

from zope.interface import implements
from scrapyd.interfaces import IPoller
from scrapyd import poller

from scrapyd_mongodb.utils import get_spider_queues


class QueuePoller(poller.QueuePoller):

    implements(IPoller)

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
