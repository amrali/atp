# Copyright 2013 Amr Ali
# See LICENSE file for details.

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

import unittest
from atp.mixin import KindSingletonMeta, UniqueSingletonMeta

class KindTmpClass(object):
    __metaclass__ = KindSingletonMeta

    def __init__(self, name):
        self.name = name

class UniqueTmpClass(object):
    __metaclass__ = UniqueSingletonMeta

    def __init__(self, name):
        self.name = name

class TestSingleton(unittest.TestCase):
    def test_kind_singleton(self):
        test1 = KindTmpClass("test1")
        test2 = KindTmpClass("test2")
        self.assertEqual(test1.name, "test1")
        self.assertEqual(test2.name, test1.name)
        self.assertEqual(test1, test2)

    def test_unique_singleton(self):
        test1 = UniqueTmpClass("test1")
        test2 = UniqueTmpClass("test2")
        self.assertEqual(test1.name, "test1")
        self.assertEqual(test2.name, "test2")
        self.assertNotEqual(test2.name, test1.name)
        self.assertNotEqual(test1, test2)

tests = [
        TestSingleton,
        ]

