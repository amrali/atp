# Copyright 2013 Amr Ali
# See LICENSE file for details.

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

import time
import unittest

try:
    import queue
except ImportError:
    # Python 2.x
    import Queue as queue

from atp.concurrency import ThreadPool, Task, Failure, async_call

class TestTask(unittest.TestCase):
    def test_task(self):
        task = Task(target=lambda x: x)
        self.assertIsInstance(task.id, long)
        self.assertEqual(task.target(True), True)
        self.assertEqual(task.success(True), True)
        self.assertEqual(task.failure(False), False)
        self.assertIsInstance(task.args, tuple)
        self.assertIsInstance(task.kwargs, dict)

class TestThreadPool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tp = ThreadPool(3, 512)
        cls.tp_results = queue.Queue()

    @classmethod
    def tearDownClass(cls):
        cls.tp.remove_all_workers(10)

    def test_async_call(self):
        t = async_call(self.__test_target, "async", success=self._test_cb,
                pool=self.tp)
        retval = self.tp_results.get(timeout=5)
        self.assertEqual(retval, "asynctest")

    def test_worker_task(self):
        t = Task(target=self.__test_target, success=self._test_cb)
        t.args = ("task1",)
        t = self.tp.run(t)
        retval = self.tp_results.get(timeout=5)
        self.assertEqual(retval, "task1test")

    def test_tp_stress(self):
        for x in range(5000):
            t = Task(target=self.__test_target)
            t.args = ("task" + str(x),)
            t = self.tp.run(t)

    def test_task_infinite(self):
        d = dict(counter = 0)
        t = Task(target=self.__test_counter, infinite=True)
        t.args = (d,)
        t = self.tp.run(t)
        time.sleep(0.01)
        t.stop()
        self.assertGreater(d['counter'], 2)

    def test_task_failure(self):
        t = Task(target=self.__test_failure, failure=self._catch_fail)
        self.tp.run(t)

    def _test_cb(self, retval):
        self.tp_results.put(retval)

    def _catch_fail(self, fail):
        with self.assertRaises(RuntimeError):
            raise fail.exception, fail.message, fail.traceback

    @staticmethod
    def __test_failure():
        raise RuntimeError

    @staticmethod
    def __test_target(arg):
        time.sleep(0.001) # 1ms
        return arg + "test"

    @staticmethod
    def __test_counter(kill_event, arg):
        arg['counter'] += 1

tests = [
        TestTask,
        TestThreadPool,
        ]

