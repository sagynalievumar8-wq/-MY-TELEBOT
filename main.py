import telebot
from telebot import types

bot = telebot.TeleBot('7908516626:AAEh4hrWMMYcEJsHvQbiroyKyNqXywiwWOQ')
#
# @bot.message_handler(commands=['start'])
# def start (message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Саламдашуу')
#     btn2 = types.KeyboardButton('Суроо беруу')
#     btn3 = types.KeyboardButton('Artka Kaituu')
#     markup.add(btn1,btn2,btn3)
#     bot.send_message(message.chat.id,
#                      text='Саламатсызбы\n Биз сизге кандай жардам бере алабыз',reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def text_obrobotka(message):
#     if (message.text == 'Саламдашуу'):
#         bot.send_message(message.chat.id, text='Privet pomposhka')
#     elif message.text == 'Суроо беруу':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton('Seni kim tuzdu')
#         btn2 = types.KeyboardButton('Sen ne kyla alasyn?')
#         btn3 = types.KeyboardButton('Artka Kaituu')
#         markup.add(btn1,btn2,btn3)
#         bot.send_message(message.chat.id, text='Ushul knopkalar menen ishteniz', reply_markup=markup)
#     if (message.text == 'Seni kim tuzdu'):
#         bot.send_message(message.chat.id, text='Alex Petrovich ')
#     elif message.text == 'Sen ne kyla alasyn?':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn2 = types.KeyboardButton('Chat gpt menen ishetendi uirotom\nhttps://chatgpt.com/')
#         btn3 = types.KeyboardButton('Artka Kaituu')
#         markup.add(btn2,btn3)
#         bot.send_message(message.chat.id, text='Akcha tap bere alam''f\nhttps://chatgpt.com/' , reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == "Artka Kaituu")
# def go_back(message):
#         bot.send_message(message.chat.id, f'siz botton chyktynyz\nkaira bashynan bashtoo uchun - (/start) basynyz', reply_markup=types.ReplyKeyboardRemove())
#
#

#
#
#
#
#
# @bot.message_handler(commands=['start'])


#
# def start(message):
#    mess = f'Здравствуйте {message.from_user.first_name}'
#    bot.send_message(message.chat.id, mess)


#
#
# @bot.message_handler(commands=['help'])
# def main (message):
#    bot.send_message(message.chat.id, 'help insta')
#
# @bot.message_handler(commands=['web'])
# def main (message):
#    bot.send_message(message.chat.id, 'help website')
#
#
# @bot.message_handler()
# def get_user(message):
#     if message.text == 'Salam':
#         bot.send_message(message.chat.id,'Salamatsyzby')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id,f"Senin aidin{message.from_user.id}")
#     elif message.text == 'Photo':
#         photo = open('media/img/photo_2025-08-12_18-29-13.jpg','rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == 'video':
#         video = open('media/video/video_2025-08-18_19-17-18.mp4', 'rb')
#         bot.send_video(message.chat.id, video)
#
#     elif message.text == 'music':
#         music = open('media/music/-_cheri_cheri_lady_-_slowed_(SkySound.cc).mp3', 'rb')
#         bot.send_audio(message.chat.id, music)
#     else:
#       bot.send_message(message.chat.id,'Men sizge tushungon jokmun')

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id,'Kakoe krasivoe photo')
#
#
# @bot.message_handler(commands=['site'])
# def web_site(message):
#     knopka= types.InlineKeyboardMarkup()
#     knopka.add(types.InlineKeyboardButton('Bat jazgyn kelse bas',url='https://monkeytype.com'))
#     bot.send_message(message.chat.id,'meni bas',reply_markup=knopka)
#
# @bot.message_handler(commands=['pogoda'])
# def pogoda_site(message):
#     knopka= types.InlineKeyboardMarkup()
#     knopka.add(types.InlineKeyboardButton('pogoda bilgin kelse bas',url='https://www.accuweather.com/en/kg/bishkek/222844/weather-forecast/222844'))
#     bot.send_message(message.chat.id,'pogoda ,bas',reply_markup=knopka)
#
# bot = TeleBot("7908516626:AAEh4hrWMMYcEJsHvQbiroyKyNqXywiwWOQ")
#
# products = {
#     " Apple": 50,
#     "Hleb": 40,
#     "Moloko": 70,
#     "masla": 175
#
# }
#
# cart = {}
#
# @bot.message_handler(commands=["start"])
# def start(msg):
#     markup = types.InlineKeyboardMarkup()
#     for item in products:
#         markup.add(types.InlineKeyboardButton(text=item, callback_data=item))
#     markup.add(types.InlineKeyboardButton(text=" Корзина", callback_data="cart"))
#     bot.send_message(msg.chat.id, "Выберите продукты:", reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == "cart":
#         result = "Ваша корзина:\n"
#         treding = 0
#         for item, count in cart.items():
#             price = products[item] * count
#             result += f"{item} x{count} = {price}som\n"
#            treding += price
#         result += f"\nИтого: {treding}som  Спасибо за продукт хорошего дня."
#         bot.send_message(call.message.chat.id, result)
#     else:
#         cart[call.data] = cart.get(call.data, 0) + 1
#         bot.answer_callback_query(call.id, f"{call.data} добавлено в корзину")
#


@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1 = types.KeyboardButton('Mechman')
    markup2 = types.KeyboardButton('Xcho')
    markup3 = types.KeyboardButton('Khalif')
    markup4 = types.KeyboardButton('Eminem')
    markup5 = types.KeyboardButton('Miyagi')
    markup6 = types.KeyboardButton('Exet')
    markup.add(markup1,markup2,markup3,markup4,markup5,markup6)
    bot.send_message(message.chat.id,
    text='Choose author',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def songs(message):
    if message.text == 'Mechman':
        music = open('media/music/Mekhman - Болен Не Тобой.mp3','rb')
        music1 = open('media/music/Mekhman - Копия Пиратская.mp3','rb')
        bot.send_audio(message.chat.id,music1)
        bot.send_audio(message.chat.id, music)
    elif message.text == 'Xcho':
        music2 = open('media/music/Xcho - Уйду.mp3','rb')
        music = open('media/music/Xcho & Macan - Memories.mp3', 'rb')
        bot.send_audio(message.chat.id,music2)
        bot.send_audio(message.chat.id, music)
    elif message.text == 'Khalif':
        music3 = open('media/music/Khalif - Азазель.mp3', 'rb')
        music = open('media/music/Khalif & Rruslan - Малефисента.mp3', 'rb')
        bot.send_audio(message.chat.id, music3)
        bot.send_audio(message.chat.id, music)
    elif message.text == 'Eminem':
        music4 = open('media/music/Eminem - Till I Collapse (ft. Nate Dogg).mp3', 'rb')
        music = open('media/music/Eminem - 97 Bonnie & Clyde.mp3', 'rb')
        bot.send_audio(message.chat.id, music4)
        bot.send_audio(message.chat.id, music)
    elif message.text == 'Miyagi':
        music5 = open('media/music/MiyaGi & Andy Panda - Minor.mp3', 'rb')
        music = open('media/music/MiyaGi & Эндшпиль - Fire Man.mp3', 'rb')
        bot.send_audio(message.chat.id, music5)
        bot.send_audio(message.chat.id, music)







class Aiidibchik:
    def __init__(self,name):
        self.name = name

        def get_info(self):
            return self.name
        A =Aiidibchik('Aidin')
        print(A.get_info())
bot.polling()



bot.polling(non_stop=True)







