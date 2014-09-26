from unittest import mock
import unittest
from service import BaseSpider


class MockConfig(object):
    def __init__(self):
        self.verbosity = None
        self.base_dir = None


class MockOS(object):
    def __init__(self):
        self.sep = "/"


class MockUUID(object):
    def __init__(self):
        self.uuid4 = None


class BaseSpiderTests(unittest.TestCase):
    def setUp(self):
        self.spider = BaseSpider(MockConfig(), mock.Mock())

    def test_generate_filename(self):
        self.spider._config.base_dir = "/tmp"
        self.spider._uuid.uuid4 = mock.Mock()
        self.spider._uuid.uuid4.return_value = "lol123"
        self.spider._os = MockOS()
        expected = "/tmp/lol123.pickle"
        self.assertEqual(self.spider._generate_filename(), expected)

    def test_generate_filename_trailing_slash(self):
        self.spider._config.base_dir = "/tmp/"
        self.spider._uuid.uuid4 = mock.Mock()
        self.spider._uuid.uuid4.return_value = "lol123"
        self.spider._os = MockOS()
        expected = "/tmp/lol123.pickle"
        self.assertEqual(self.spider._generate_filename(), expected)