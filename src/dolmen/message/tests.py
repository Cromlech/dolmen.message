# -*- coding: utf-8 -*-
"""Test harness"""

import doctest
import unittest
import grokcore.message

from cromlech.io.testing import TestRequest


def test_suite():
    suite = unittest.TestSuite()
    test = doctest.DocFileSuite(
        'README.txt', optionflags=doctest.ELLIPSIS)
    suite.addTest(test)
    return suite
