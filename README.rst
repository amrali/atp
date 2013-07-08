Adaptive Thread Pool
====================

An adaptive thread pool implementation that offers you a configurable **minimum**
number of threads to be always available during the application's lifetime.
This implementation adapts to the thread consumption rate by having a pool volume
monitoring thread increasing the number of workers to accommodate the rate of tasks
submitted to the pool. Workers that sleep for a configurable period of time due to
the lack of tasks will be terminated.

Installation
------------

It's trivial to install it, all you have to do is::

    pip install atp

Usage
-----

You will need to initialize a thread-pool before using any of the helper functions
or passing a Task to be processed by a worker. There are two ways to use this
library, you could either initialize a global thread pool or initialize a local
thread pool::

    import atp

    # The ``min_workers`` argument specifies the minimum number of workers in the
    # pool, the default is 2.
    # The ``stack_size`` argument specifies the stack size of each thread in KiB,
    # the default value is 512.

    # Initialize the global thread pool
    atp.GlobalThreadPool(min_workers = 2, stack_size = 512)

    # Or initialize a local thread pool
    tp = atp.ThreadPool(min_workers = 2, stack_size = 512)

There are two interfaces to pass tasks to workers. You could either create a ``Task``
class manually and pass it to the thread-pool or use the helper functions::

    import atp

    # Create a task manually.
    task = atp.Task(target=<callable>, success=<callable>, args=(1,2,3,),
            kwargs={'a':1, 'b':2})
    atp.GlobalThreadPool().run(task)

    # Run a task through helpers. Note that you can pass your own local thread-pool
    # to the helper function through the ``pool`` argument. The ``args`` and ``kwargs``
    # are the arguments and keyword arguments passed to the target functions.
    task = atp.async_call(<callable>, success=<callable>, args=(1,2,3,),
            kwargs={'a':1, 'b':2}, pool=atp.GlobalThreadPool())

There are two types of tasks you could pass to the thread pool; a one-time-run task
and an infinite task. The former is when you need a worker to run a task only once
but the latter is when you need to run a task infinitely many times::

    import atp
    import time

    def print_string(string):
        print string

    def caps(string):
        return string.upper()

    task = atp.async_call(caps, 'hello world!', success=print_string)
    time.sleep(0.1) # 100ms

A task that will run indefinitely will be passed an event as a first argument to
check on in case you wanted it to stop::

    import atp
    import time

    result = [1]

    def increase(kill, arg):
        while not kill.is_set() and arg[-1] < 100:
            arg.append(arg[-1] + 1)

    task = atp.async_call(increase, result, infinite=True)
    time.sleep(0.1) # 100ms
    task.stop()
    assert len(result) == 100

In case of a task throwing an unhandled exception the failure callback will catch
the exception and wrap it in a ``Failure`` class where you can access all the
exception's details. If the failure callback throws an unhandled error it will be
caught and logged::

    import atp
    import time
    import logging

    logging.getLogger().addHandler(logging.StreamHandler())

    def will_fail():
        throw RuntimeError("fake error")

    def catch_fail(error):
        throw error.exception, error.message, error.traceback

    task = atp.async_call(will_fail, failure=catch_fail)
    time.sleep(0.1) # 100ms

Hacking
-------

Thought of something you would like to see in ATP? You can visit the `issue tracker`_
to check if it was reported before, and if not you are encouraged to create
an issue or feature request first to discuss it. When you are ready to contribute
code or documentation fork the `code repository`_ at github_.

To get started clone your fork and setup your environment::

    $ git clone git@github.com:<your username>/atp.git
    $ cd atp/
    $ virtualenv venv
    $ source venv/bin/activate
    $ python setup.py develop

Copying
-------

Free use of this software is granted under the terms of the GNU General Public
License (GPLv3+). For details see the ``LICENSE`` file included with this
distribution.

.. _code repository: https://github.com/amrali/atp
.. _issue tracker: https://github.com/amrali/atp/issues
.. _github: https://github.com/

