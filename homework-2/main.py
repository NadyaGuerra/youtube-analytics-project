from src.channel import Channel

if __name__ == '__main__':
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

    # получаем значения атрибутов

   # print(vdud.title)  # вДудь
   # print(vdud.videoCount)  # 163 (может уже больше)
    #print(vdud.url)  # https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

    # менять не можем
    #vdud.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    #print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'vdud.json' в данными по каналу
    #vdud.to_json('vdud.json')
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    redactsiya = Channel('UC1eFXmJNkjITxPFWTy6RsWg')

    # Используем различные магические методы
    print(vdud)  # 'вДудь (https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA)'
    print(vdud + redactsiya)  # 13970000
    print(vdud - redactsiya)  # 6630000
    print(redactsiya - vdud)  # -6630000
    print(vdud > redactsiya)  # True
    print(vdud >= redactsiya)  # True
    print(vdud < redactsiya)  # False
    print(vdud <= redactsiya)  # False
    print(vdud == redactsiya)  # False