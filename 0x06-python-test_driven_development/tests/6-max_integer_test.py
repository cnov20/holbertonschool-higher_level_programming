#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_int_list(self):
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_arg_number(self):
        self.assertEqual(max_integer([1000000000000000,
                                  1, 2, 3]), 1000000000000000)


    def test_no_input(self):
        self.assertIsNone(max_integer())

    def test_empty_matrix(self):
        self.assertIsNone(max_integer([]))

    def test_list_only_none(self):
        self.assertIsNone(max_integer([None]))

    @unittest.expectedFailure
    def test_mix_list(self):
        self.assertEqual(max_integer([c, 4, 5, 6]), "broken")

    @unittest.expectedFailure
    def test_str(self):
        self.assertEqual(max_integer('Snow'), "broken")

    @unittest.expectedFailure
    def test_str_in_list(self):
        self.assertEqual(max_integer([5, 'cool']), "broken")

    @unittest.expectedFailure
    def test_only_int(self):
        self.assertEqual(max_integer(1020), "broken")

    @unittest.expectedFailure
    def test_only_float(self):
        self.assertEqual(max_integer(8.5), "broken")

    @unittest.expectedFailure
    def test_float_list(self):
        self.assertEqual(max_integer([5.8, 5.6, 3.4]), "broken")

    @unittest.expectedFailure
    def test_just_boolean_t(self):
        self.assertEqual(max_integer(True))
