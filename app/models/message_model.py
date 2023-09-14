from ..database import DatabaseConnection

class Message:
    def __init__(self, **kwargs) -> None:
        self.message_id = kwargs.get('message_id', None)
        self.message_body = kwargs.get('message_body', None)
        self.user_id = kwargs.get('user_id', None)
        self.channel_id = kwargs.get('channel_id', None)
        self.creation_date = kwargs.get('creation_date', None)
        self.update_date = kwargs.get('update_date', None)
        
    @classmethod
    def get_message(cls, msg_id):
        query = "SELECT * FROM messages WHERE message_id = %s"
        msg = DatabaseConnection.fetch_one(query, (msg_id,))
        if msg is not None:
            return Message(
                message_id = msg[0],
                message_body = msg[1],
                user_id = msg[2],
                channel_id = msg[3],
                creation_date = msg[4],
                update_date = msg[5]
            )
        return None

    @classmethod
    def get_messages(cls, channel_id) -> list['Message']:
        query = "SELECT * FROM messages WHERE channel_id = %s"
        msgs = DatabaseConnection.fetch_all(query, (channel_id,))
        
        msg_list = []
        for msg in msgs:
            msg_data = Message(
                message_id = msg[0],
                message_body = msg[1],
                user_id = msg[2],
                channel_id = msg[3],
                creation_date = msg[4],
                update_date = msg[5]
            )
            msg_list.append(msg_data)
        
        return msg_list

    @classmethod
    def exist(cls, msg_id: int):
        query = "SELECT 1 FROM messages WHERE message_id = %s"
        result = DatabaseConnection.fetch_one(query, (msg_id,))
        return result is not None
    
    def serialize(self):
        return {
            'message_id': self.message_id,
            'message_body': self.message_body,
            'user_id': self.user_id,
            'channel_id': self.channel_id,
            'creation_date': self.creation_date,
            'update_date': self.update_date
        }