# coding: utf-8

import unittest

from tapioca_jarbas import Jarbas


class TestTapiocaJarbas(unittest.TestCase):

    def setUp(self):
        self.wrapper = Jarbas()


if __name__ == '__main__':
    unittest.main()
