from abc import abstractmethod
import os
import pickle
import uuid


class BaseSpider(object):
    def __init__(self, config, log):
        """
        :type config:   model.Config()
        :type log:      logging.getLogger()

        """
        self._log = log
        self._config = config
        self._os = os
        self._uuid = uuid
        self._pickle = pickle

    @abstractmethod
    def crawl(self, **kwargs):
        """
        This method can ONLY accept keyword arguments. BaseSpider.save() should be called at some
        point during its execution.

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
        self._log.debug("Writing to file: " + str(filename))
        with open(filename, "wb+") as f:
            pickle.dump(data, f)

    def _generate_filename(self):
        """
        Randomly generates a filename and returns a full path based on the directory
        specified in the configuration object.

        """
        directory = self._config.base_dir
        if not self._config.base_dir.endswith(self._os.sep):
            directory += self._os.sep
        return directory + str(self._uuid.uuid4()) + ".pickle"