class GenericErrorException(Exception):

    """ Exception raised when an some occures error """

    def __init__(self, message='An error occures'):
        self.message = message
        super().__init__(self.message)