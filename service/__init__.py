from abc import abstractmethod
import logging
import os
import pickle
from uuid import uuid4


class BaseSpider(object):
    def __init__(self, config):
        self._directory = None
        self._filename = 0
        self._log = None
        self._config = config
        self._os = os
        self._uuid4 = uuid4
        self._pickle = pickle

    @abstractmethod
    def crawl(self, *args, **kwargs):
        raise NotImplemented

    def save(self, data, custom_filename=None):
        """
        :param data:    the results from crawling some resource
        :type data:     dict
        :param custom_filename:    If not manually set, files will be given incrementing numbers as filenames
        :type custom_filename:     str

        """
        assert isinstance(data, dict)
        filename = custom_filename if custom_filename is not None else self._get_next_filename()
        with open(self._get_directory() + filename, "wb+") as f:
            pickle.dump(data, f)

    @property
    def log(self):
        if self._log is None:
            self._log = logging.getLogger("spider")
            self._log.addHandler(logging.StreamHandler)
            self._log.setLevel(self._get_log_level())
        return self._log

    def _get_directory(self):
        """
        Chooses a directory name and creates it, if that hasn't been done, and
        returns the full path with a trailing slash.

        """
        if self._directory is None:
            directory = self._generate_directory_name()
            try:
                self._os.makedirs(directory)
            except OSError:
                pass
            finally:
                self._directory = directory
        return self._directory

    def _generate_directory_name(self):
        return self._config.base_dir + self._os.sep + str(self._uuid4()) + self._os.sep

    def _get_log_level(self):
        """
        Interprets the verbosity command line argument and returns an integer that's meaningful to logger.setLevel()

               60 (silent)
        -v     50 (logging.CRITICAL)
        -vv    40 (logging.ERROR)
        -vvv   30 (logging.WARN)
        -vvvv  20 (logging.INFO)
        -vvvvv 10 (logging.DEBUG)

        """
        # Starting with 60 (which will turn off all logging), decrease the level by 10 for each 'v' supplied by the user
        # The lower the number, the more verbose the logging will be
        return 60 - self._config.verbosity * 10

    def _get_next_filename(self):
        self._filename += 1
        return str(self._filename)