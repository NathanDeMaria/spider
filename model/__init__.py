class Config(object):
    """
    A configuration object set by command line, for now.

    """
    def __init__(self):
        self._base_dir = None
        self._verbosity = 5  # defaults to debug mode

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
        return 60 - self._verbosity * 10

    @verbosity.setter
    def verbosity(self, value):
        if value is None or not isinstance(value, int):
            raise ValueError("Invalid log level setting")
        self._verbosity = value