# -*- coding: utf-8 -*-

from twisted.application.service import Application
from twisted.application.internet import TimerService, TCPServer
from twisted.web import server
from twisted.python import log

from scrapy.utils.misc import load_object

from scrapyd.interfaces import IEggStorage, IPoller, ISpiderScheduler, IEnvironment
from scrapyd.eggstorage import FilesystemEggStorage
from scrapyd.environ import Environment
from scrapyd.website import Root

from scrapyd_mongodb.poller import QueuePoller
from scrapyd_mongodb.scheduler import SpiderScheduler


def get_application(config):
    app = Application('Scrapyd')
    http_port = config.getint('http_port', 6800)
    bind_address = config.get('bind_address', '0.0.0.0')
    poll_interval = config.getfloat('poll_interval', 5)

    poller = QueuePoller(config)
    eggstorage = FilesystemEggStorage(config)
    scheduler = SpiderScheduler(config)
    environment = Environment(config)

    app.setComponent(IPoller, poller)
    app.setComponent(IEggStorage, eggstorage)
    app.setComponent(ISpiderScheduler, scheduler)
    app.setComponent(IEnvironment, environment)

    laupath = config.get('launcher', 'scrapyd.launcher.Launcher')
    laucls = load_object(laupath)
    launcher = laucls(config, app)

    timer = TimerService(poll_interval, poller.poll)
    webservice = TCPServer(http_port, server.Site(Root(config, app)), interface=bind_address)
    log.msg(format='Scrapyd web console available at http://%(bind_address)s:%(http_port)s/',
            bind_address=bind_address, http_port=http_port)

    launcher.setServiceParent(app)
    timer.setServiceParent(app)
    webservice.setServiceParent(app)

    return app
