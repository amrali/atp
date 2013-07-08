#!/usr/bin/env python
# Copyright 2013 Amr Ali
# See LICENSE file for details.

__author__ = "Amr Ali"
__copyright__ = "Copyright 2013 Amr Ali"
__license__ = "GPLv3+"
__email__ = "amr.ali.cc@gmail.com"

# Make sure setuptools is installed
from distribute_setup import use_setuptools
use_setuptools()

import os
from setuptools import setup, find_packages
from atp import __version__

BASE_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(BASE_DIR, 'README.rst')
REQS_PATH = os.path.join(BASE_DIR, 'requirements.txt')

with open(README_PATH, 'rb') as fd:
    README = fd.read()

classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    ]

setup(
        name = 'atp',
        version = __version__,
        description = 'An adaptive thread pool implementation',
        long_description = README,
        author = 'Amr Ali',
        author_email = 'amr.ali.cc@gmail.com',
        maintainer = 'Amr Ali',
        maintainer_email = 'amr.ali.cc@gmail.com',
        url = 'https://github.com/amrali/atp',
        packages = find_packages(),
        test_suite = 'atp.load_test_suite',
        license = 'GPLv3+',
        platforms = 'Posix',
        classifiers = classifiers,
    )

