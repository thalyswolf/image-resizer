class GenericErrorException(Exception):

    """ Exception raised when an some occures error """

    def __init__(self, message='An error occures'):
        self.message = message
        super().__init__(self.message)

class InvalidHeightErrorException(Exception):

    """ Exception raised when the height informed is invalid """

    def __init__(self, message='the height is invalid'):
        self.message = message
        super().__init__(self.message)

class InvalidWidthErrorException(Exception):

    """ Exception raised when the width informed is invalid """

    def __init__(self, message='the width is invalid'):
        self.message = message
        super().__init__(self.message)

class InvalidFileMimeErrorException(Exception):

    """ Exception raised when the file format is not accepted """

    def __init__(self, message='the mime is invalid'):
        self.message = message
        super().__init__(self.message)
class InvalidFileDataErrorException(Exception):

    """ Exception raised when the file data is malformed """

    def __init__(self, message='the file data is invalid'):
        self.message = message
        super().__init__(self.message)

