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
__version__ = '1.2.0-r'

import logging
import urllib.error

from .SqliteDb import *
from .PostgresDb import *
from .User import *
from typing import NamedTuple, Literal
from urllib import request


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    hotfix: int
    releaseLevel: Literal["alpha", "beta", "candidate", "final"]


version_info: VersionInfo = VersionInfo(major=1, minor=2, micro=0, hotfix=0, releaseLevel='final')

logging.getLogger(__name__).addHandler(logging.NullHandler())


def connectionTest():
    try:
        request.urlopen('https://google.com', timeout=5)
    except request.HTTPError:
        import warnings

        warnings.warn(
            "\nSeems like there's no internet connection.\n"
            " 'https://google.com' cannot be pinged.\n"
            " App will continue to run without connection, but some functions may be missing or broken.",
        )
    except urllib.error.URLError:
        import warnings
        warnings.warn("\nSeems like there's no internet connection.\n"
                      "'https://google.com' cannot be pinged.\n"
                      "App will continue to run without connection, but some functions may be missing or broken.")


connectionTest()
del logging, NamedTuple, Literal, VersionInfo
