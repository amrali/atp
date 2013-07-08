# Copyright 2013 Amr Ali
# See LICENSE file for details.

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

import sys
from collections import defaultdict

def public(obj):
    """A decorator to avoid retyping function/class names in __all__."""
    _all = sys.modules[obj.__module__].__dict__.setdefault('__all__', [])
    if obj.__name__ not in _all:
        _all.append(obj.__name__)
    return obj

class SingletonAbstractMeta(type):
    """A Singleton pattern abstract metaclass."""

    def __init__(cls, name, bases, attrs):
        super(SingletonAbstractMeta, cls).__init__(name, bases, attrs)
        cls._instance = defaultdict(str)

    def __call__(cls, *args, **kwargs):
        key = cls._make_key(*args, **kwargs)
        if key not in cls._instance:
            cls._instance[key] = super(SingletonAbstractMeta, cls).__call__(
                    *args, **kwargs)
        return cls._instance[key]

    @classmethod
    def _make_key(cls, *args, **kwargs):
        """A function responsible for generating a key to check against and see
        if an instance was already constructed for that key.

        This is an abstract function, it is required to override it.
        """
        from atp.excepts import ATPUnimplementedError
        raise ATPUnimplementedError("function _make_id is not implemented")

@public
class KindSingletonMeta(SingletonAbstractMeta):
    """A singleton pattern metaclass that uses the underlying class' name
    as the unique constraint.
    """

    @classmethod
    def _make_key(cls, *args, **kwargs):
        return cls.__class__

@public
class UniqueSingletonMeta(SingletonAbstractMeta):
    """A Singleton pattern metaclass that uses arguments passed to the
    underlying class constructor as the unique constraint.
    """

    @classmethod
    def _make_key(cls, *args, **kwargs):
        key = ''
        for arg in args:
            try:
                key += str(arg)
            except:
                continue
        for kwarg, value in kwargs.iteritems():
            try:
                key += str(kwarg) + str(value)
            except:
                continue
        return key

