# Copyright 2013 Amr Ali
# See LICENSE file for details.

"""
An adaptive thread pool implementation that offers you a configurable **minimum**
number of threads to be always available during the application's lifetime.
This implementation adapts to the thread consumption rate by having a pool volume
monitoring thread increasing the number of workers to accommodate the rate of tasks
submitted to the pool. Workers that sleep for a configurable period of time due to
the lack of tasks will be terminated.
"""

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

import logging

from .concurrency import Task, ThreadPool, GlobalThreadPool, async_call
from .version import __version__

def load_test_suite():
    from .test import suite
    return suite

logging.getLogger("atp").addHandler(logging.NullHandler())

