# -*- coding: utf-8 -*-

from scrapyd.utils import get_project_list

from scrapyd_mongodb.spiderqueue import MongoDBSpiderQueue


def get_spider_queues(config):
    """Return a dict of Spider Quees keyed by project name"""
    queues = {}
    for project in get_project_list(config):
        collection = '{}_queue'.format(project)
        queues[project] = MongoDBSpiderQueue(config, collection)
    return queues
