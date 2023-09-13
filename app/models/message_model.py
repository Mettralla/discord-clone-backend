from ..database import DatabaseConnection

class Message:
    def __init__(self, **kwargs) -> None:
        self.message_id = kwargs.get('message_id', None)