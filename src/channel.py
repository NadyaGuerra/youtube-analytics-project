from googleapiclient.discovery import build
import os
import json



class Channel:
    """Класс для ютуб-канала"""
    #api_key: str = os.getenv("YT_API_KEY")
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key: str = os.getenv("YT_API_KEY")
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

