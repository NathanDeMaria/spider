from abc import abstractmethod
import logging
import os
import pickle
from uuid import uuid4


class BaseSpider(object):
    def __init__(self, config):
        self._log = None
        self._config = config
        self._os = os
        self._uuid4 = uuid4
        self._pickle = pickle

    @abstractmethod
    def crawl(self, **kwargs):
        """
        This method can ONLY accept keyword arguments.

        """
        raise NotImplemented

    def save(self, data):
        """
        Write the results to disk as a serialized string.

        :param data:    the results from crawling some resource
        :type data:     dict

        """
        assert isinstance(data, dict)
        filename = self._generate_filename()
        self.log.debug("Writing to file: " + str(filename))
        with open(filename, "wb+") as f:
            pickle.dump(data, f)

    @property
    def log(self):
        if self._log is None:
            self._log = logging.getLogger("spider")
            self._log.addHandler(logging.StreamHandler)
            self._log.setLevel(self._config.verbosity)
        return self._log

    def _generate_filename(self):
        """
        Randomly generates a filename and returns a full path based on the directory
        specified in the configuration object.

        """
        return self._config.base_dir + self._os.sep + str(self._uuid4()) + ".pickle"