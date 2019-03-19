"""Tests for worry free YAML config files
"""
from __future__ import division, absolute_import, print_function

import os
import os.path
import stat
import shutil
import re
import unicodedata
import sys
import time
import unittest

from test import _common
from test._common import item
import beets.library
import beets.mediafile
import beets.dbcore.query
from beets import util
from beets import plugins
from beets import config
from beets.mediafile import MediaFile
from beets.util import syspath, bytestring_path
from test.helper import TestHelper
import six

# Shortcut to path normalization.
np = util.normpath

# mock view for confit tests
class MockView():
    def __init__(self, name):
        self.name = name

# confit tests
class ConfitTest(unittest.TestCase):
    # tests for 2 configuration directories
    def test_config_dirs(self):
        e = beets.util.confit.config_dirs()
        self.assertEquals(len(e), 2)

    def test_FloatToInteger_convert(self):
        ic = beets.util.confit.Integer()
        val = ic.convert(5.26, {})
        self.assertEquals(val, 5)

    def test_bad_convert(self):
        ic = beets.util.confit.Integer()
        try:
            # trigger an exception
            mv = MockView("testing")
            val = ic.convert(None, mv)
            self.assertTrue(False)
        except:
            # eat the exception
            self.assertTrue(True)
