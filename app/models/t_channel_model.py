from ..database import DatabaseConnection

class Channel:
    def __init__(self, **kwargs):
        self.channel_id = kwargs.get("channel_id", None)
        self.channel_name = kwargs.get("channel_name", None)
        self.user_id = kwargs.get("user_id", None)
        self.server_id = kwargs.get("server_id", None)
    
    @classmethod
    def create_channel(cls, channel: 'Channel'):
        query = "INSERT INTO channels (channel_name, user_id, server_id) VALUES (%s, %s, %s)"
        params = (channel.channel_name, channel.user_id, channel.server_id)
        DatabaseConnection.execute_query(query, params)
        
    @classmethod
    def get_channels_from_server(cls, server_id) -> list['Channel']:
        query = "SELECT channel_id, channel_name, user_id, server_id FROM channels WHERE server_id = %s"
        channels = DatabaseConnection.fetch_all(query, (server_id,))
        
        channels_list = []
        for channel in channels:
            ch_data = Channel(
                channel_id = channel[0],
                channel_name = channel[1],
                user_id = channel[2],
                server_id = channel[3],
            )
            channels_list.append(ch_data)
        
        return channels_list
        
    @classmethod
    def exists_name(cls, channel_name):
        """Check Exists Server Name"""
        query = "SELECT 1 FROM channels WHERE channel_name = %s"
        result = DatabaseConnection.fetch_one(query, (channel_name,))
        return result is not None
    
    def serialize(self):
        return {
            "channel_id": self.channel_id,
            "channel_name": self.channel_name,
            "user_id": self.user_id,
            "server_id": self.server_id
        }