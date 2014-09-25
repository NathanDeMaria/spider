import unittest
from model import Config
import logging


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_verbosity_default(self):
        self.assertEqual(self.config.verbosity, logging.DEBUG)

    def test_verbosity_3(self):
        self.config.verbosity = 3
        self.assertEqual(self.config.verbosity, logging.WARN)

    def test_verbosity_2(self):
        self.config.verbosity = 2
        self.assertEqual(self.config.verbosity, logging.ERROR)

    def test_invalid_base_dir(self):
        with self.assertRaises(ValueError):
            self.config.base_dir = ""