class EdiaException(Exception):
    message = None

    def __init__(self, message: str | None = None, *args):
        super().__init__(args)
        if message is None and self.message is None:
            raise NotImplementedError('Please define some exception message.')
        self._message = message or self.message

    def __repr__(self):
        return self._message


class ObjectNotInitialized(EdiaException):
    message = 'Instance of this class not initialized.'
