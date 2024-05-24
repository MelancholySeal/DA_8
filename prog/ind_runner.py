#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import ind_tests


if __name__ == "__main__":
    ind_test_suite = unittest.TestSuite()
    ind_test_suite.addTest(unittest.makeSuite(ind_tests.indTest))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(ind_test_suite)
