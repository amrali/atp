# Copyright 2013 Amr Ali
# See LICENSE file for details.

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

import sys

from atp.mixin import public

@public
def reraise(ex, message=None):
    """Reraise the exception last happened with the original traceback.

    :param ex:
        The exception to be raised instead of the original one.
    :type ex:
        A subclass of Exception.
    :param message:
        An optional message to replace the old exception's message.
    :type message:
        str
    :raises:
        ``ex``
    """
    (_, msg, tb) = sys.exc_info()
    msg = message if message else msg
    raise (ex, msg, tb)

@public
class ATPException(Exception):
    """An ATP general exception"""
    pass

@public
class ATPUnimplementedError(ATPException):
    """An unimplemented operation error"""
    pass

@public
class ATPTaskError(ATPException):
    """A task operation error"""
    pass

@public
class ATPThreadPoolError(ATPException):
    """A thread-pool operation error"""
    pass

