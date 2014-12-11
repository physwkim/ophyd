#!/usr/bin/env python2.7
'''
An example of using :class:`caServer`, an EPICS channel access server
implementation based on pcaspy
'''
from __future__ import print_function
import time

import config

from ophyd.utils.cas import (caServer, PythonPV)
from ophyd.controls import EpicsSignal


def test():
    loggers = ('ophyd.utils.cas',
               )

    config.setup_loggers(loggers)

    pvname = config.fake_pvnames[0]

    session = config.session
    server = session.cas

    def updated(value=None, **kwargs):
        print('Updated to: %s' % value)

    python_pv = PythonPV(pvname, 123.0, server=server)
    signal = EpicsSignal(pvname)
    signal.subscribe(updated)

    time.sleep(0.1)

    for i in range(10):
        python_pv.value = i
        time.sleep(0.05)


if __name__ == '__main__':
    test()
