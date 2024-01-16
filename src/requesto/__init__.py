"""
Requesto-py
Psycopg2/Sqlite3 API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Psycopg2/Sqlite3.

:copyright: (c) 2023-present SOLIDusr
:license: GNU GPL, see LICENSE for more details.

"""

__title__ = 'requesto'
__author__ = 'SOLIDusr'
__license__ = 'GNU'
__copyright__ = 'Copyright 2023-present SOLIDusr'
__version__ = '1.1.0-r'

import logging
from .requesto import *
from typing import NamedTuple, Literal
from urllib import request


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    hotfix: int
    releaseLevel: Literal["alpha", "beta", "candidate", "final"]


version_info: VersionInfo = VersionInfo(major=1, minor=1, micro=0, hotfix=0, releaseLevel='beta')

logging.getLogger(__name__).addHandler(logging.NullHandler())


def connectionTest():
    try:
        request.urlopen('https://google.com', timeout=5)
    except request.HTTPError:
        import warnings

        warnings.warn(
            "Seems like there's no internet connection."
            " 'https://google.com' cannot be pinged."
            " App will continue to run without connection, but some functions may be missing.",
        )


connectionTest()
del logging, NamedTuple, Literal, VersionInfo
