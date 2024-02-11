#!/usr/bin/python3

import unittest
from pycodestyle_compliant import add_integer

class TestAddIntegerFunction(unittest.TestCase):

    def test_add_integer(self):
        with self.assertRaises(TypeError):
            add_integer("2", 3)
        with self.assertRaises(TypeError):
            add_integer(2, "3")
        with self.assertRaises(TypeError):
            add_integer("2", "3")
        with self.assertRaises(TypeError):
            add_integer(True, 3)
        with self.assertRaises(TypeError):
            add_integer(2, None)
        self.assertEqual(add_integer(2, 3), 5)
        self.assertEqual(add_integer(-1, 5), 4)
        self.assertEqual(add_integer(0, 0), 0)
        self.assertEqual(add_integer(-1, -1), -2)
        self.assertEqual(add_integer(2.5, 3.5), 5)
        self.assertEqual(add_integer(-1.7, 5.2), 3)
        self.assertEqual(add_integer(0.5, 0.5), 0)
        self.assertEqual(add_integer(-1.1, -1.9), -2)
        self.assertEqual(add_integer(2, 3.5), 5)
        self.assertEqual(add_integer(-1.7, 5), 3)
        self.assertEqual(add_integer(0, 0.5), 0)
        self.assertEqual(add_integer(-1.1, -1), -2)

if __name__ == '__main__':
    unittest.main()
