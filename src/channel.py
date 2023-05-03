from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id  # private
        self.__channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.title = self.__channel["items"][0]["snippet"]["title"]
        self.description = self.__channel["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA/{self.__channel_id}'
        self.__subscriberCount = int(self.__channel["items"][0]["statistics"]["subscriberCount"])
        self.videoCount = self.__channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.__channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """возвращает id канала"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    @property
    def subscriberCount(self) -> int:
        """возвращает количество подписчиков"""
        return self.__subscriberCount

    @classmethod
    def get_service(cls):
        """возвращает обьект для работы с API"""
        return cls.youtube

    def to_json(self, filename):
        """возвращает значение атрибутов класса в файл json"""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriberCount,
            'video_count': self.videoCount,
            'views_count': self.viewCount
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def __str__(self):
        return f'{self.title}-({self.url})'

    def __add__(self, other: 'Channel'):
        """
        Метод сложения.
        """
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other: 'Channel'):
        """
        Метод вычитания.
        """
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other: 'Channel'):
        """
        Метод сравнения больше.
        """
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other: 'Channel'):
        """
        Метод сравнения больше или равно.
        """
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other: 'Channel'):
        """
        Метод сравнения меньше.
        """
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other: 'Channel'):
        """
        Метод сравнения меньше или равно.
        """
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other: 'Channel'):
        """
        Метод сравнения.
        """
        return self.subscriberCount == other.subscriberCount


