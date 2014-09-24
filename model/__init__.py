class Config(object):
    """
    A configuration object set by command line, for now.

    """
    def __init__(self):
        self._base_dir = None
        self._verbosity = None

    @property
    def base_dir(self):
        return self._base_dir

    @base_dir.setter
    def base_dir(self, value):
        if value is None or not value:
            raise ValueError("You need to set a valid base directory")
        self._base_dir = value

    @property
    def verbosity(self):
        """
        The number of v's specified on the command line (e.g. -vvvv == 4)
        """
        return self._verbosity

    @verbosity.setter
    def verbosity(self, value):
        if value is None or not isinstance(value, int):
            raise ValueError("Invalid log level setting")
        self._verbosity = value