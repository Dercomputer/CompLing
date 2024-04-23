from random import randint
import vk_api
from datetime import date, datetime

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(
    token="vk1.a.1sB-pCMjJduVXzZY_a5nV7OKTYQmzt4Wz5jb1x6uPxTFCh-3F6Hcs5TH2bAl0Q1AmTvgLz4zF42HXSWmBfZCK6U3Pgy4E30_EsWbZ6Pc5kcvqbTg2URVeTOVfgfPDvf61VYdb2jHTJ3yOCdDNn2anFwN39VbpSQDedLCMUNpEOrwQAnBx1WsrgZa5QFVmAd-uwk_cSdfuthKOWrDqFgKEw")
longpoll = VkBotLongPoll(vk_session, 225670086)
vk = vk_session.get_api()
lst = ["привет", "как дела", "какое сегодня число", "точное время", "счастливое число"]


def lst_see():
    output = ''
    for i in range(len(lst)):
        output += ''.join(lst[i]) + '\n'
    return output


def main():
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message["text"].lower() == "привет":
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message="Привет! Я бот сделанный для имитации человека)")
            elif event.obj.message["text"].lower() == "как дела?" or event.obj.message["text"].lower() == "как дела":
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message="хорошо, а у тебя?)")
            elif event.obj.message["text"].lower() in ["плохо", "неочень", "такое"]:
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message="что случилось?((")
            elif event.obj.message["text"].lower() in ["всё хорошо", "отлично", "хорошо", "круто", "нормально"]:
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message="это радует")
            elif event.obj.message["text"].lower() in ["не хочу говорить", "отстань", "лучше чем у тебя"]:
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message="бяка")
            elif event.obj.message["text"].lower() == "какое сегодня число?" or event.obj.message[
                "text"].lower() == "какое сегодня число":
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message=f"{date.today()}")
            elif event.obj.message["text"].lower() == "точное время":
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message=f"{datetime.now().time()}")
            elif event.obj.message["text"].lower() == "счастливое число":
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0,
                                 message=f"Ваше счастливое число - {randint(1, 101)}")
            elif event.obj.message["text"].lower()  in ["список запросов", "список команд", "начать"]:
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0, message=f"{lst_see()}")
            else:
                vk.messages.send(peer_id=event.obj.message["from_id"], random_id=0,
                                 message="Я не знаю такой команды, обратитесь к списку команд, для этого напишите "
                                         "'список команд'")


if __name__ == "__main__":
    main()
