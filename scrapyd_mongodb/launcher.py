# -*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.python import log
from scrapyd import launcher


class Launcher(launcher.Launcher):

    def _spawn_process(self, message, slot):
        super(Launcher, self)._spawn_process(message, slot)
        process = self.processes[slot]
        timeout = getattr(process.spider, 'timeout', None)
        if timeout:
            log.msg('Spider has timeout of {} min'.format(timeout))
            timeout = process.spider.timeout * 60.0
            reactor.callLater(timeout, self.kill_process, process)

    def kill_process(self, process):
        log.msg('Kill: "{}"'.format(dir(process)))
