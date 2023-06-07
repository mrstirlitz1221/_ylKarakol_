# -*- coding: utf-8 -*-
import logging, asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
logging.basicConfig(level=logging.INFO)

TOKEN = '5589637928:AAHcmO9i8wlGWLFU4A-vDApTJV9KJrC_4R4'
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = 1138500722

"""
Кнопки
"""

def create_menu_markup():
    buttons = [
        [InlineKeyboardButton(text="ℹ️Информация", callback_data="info")],
        [InlineKeyboardButton(text="🌱Команда Young Life", callback_data="yl")],
        [InlineKeyboardButton(text="🌐Наш Instagram", url="instagram.com/yl_karakol/")],
        [InlineKeyboardButton(text="❓Помощь", callback_data="help")]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def peples():
    buttons = [
        [InlineKeyboardButton(text='Дарья', callback_data='Дарья'), InlineKeyboardButton(text='София', callback_data='София')],
        [InlineKeyboardButton(text='Саида', callback_data='Саида'), InlineKeyboardButton(text='Луиза', callback_data='Луиза')],
        [InlineKeyboardButton(text='Макс', callback_data='Макс'), InlineKeyboardButton(text='СФ-Даня', callback_data='СФ-Даня')],
        [InlineKeyboardButton(text='◀Назад', callback_data='back_menu')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

"""
Главное меню и обробатчики главного меню
"""

@dp.message_handler(commands=['start'])
async def handle_start(message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    user_name = message.from_user.first_name
    add_user_to_db(user_id, username, user_name)
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHaNNjz6fNgCKO1lJquLojxaswZ_-xNwACxiAAAlIX6Emi2MpPVYk8qy0E')
    await bot.send_message(message.chat.id, f'Привет, <b><u>{message.from_user.full_name}</u></b>', parse_mode='html')
    await bot.send_message(message.chat.id, "Выберите действие:", reply_markup = create_menu_markup())

@dp.callback_query_handler(lambda query: query.data == 'info')
async def handle_info(call) -> None:
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f'<i><span class="tg-spoiler">Young Life - это место, где тебя ждут, место где тебя ценят и место где тебе не будет скучно!\n\nМы те, кто организовывает разнообразные увлекательные мероприятия для молодёжи и подростков! Квесты, лагеря, сумашедшие вечера и это ещё не всё!\n\nYoung Life - это там, где тебя поймут и выслушают, место встречи друзей, хорошее общение и просто там, где можно отлично провести время в хорошей компании за чашкой чая или миской поп-корна смотря фильм.\n\nРазные интересные и захватывающие настольные игры и другие разнообразные виды времяпрепровождения не дадут тебе скучать!</span></i>',parse_mode='html', reply_markup=create_back_button())

@dp.callback_query_handler(lambda query: query.data == 'help')
async def handle_help(call):
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''По вопросам бота писать @YLKarakol_Help''',reply_markup=create_back_button())

@dp.callback_query_handler(lambda query: query.data == 'yl')
async def handle_yl(call):
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="О ком хотите узнать:",reply_markup=peples())

"""
Функции Назад
"""

def create_back_button():
    back_button = [
        [InlineKeyboardButton(text='◀Назад', callback_data='back_menu')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=back_button)

@dp.callback_query_handler(lambda query: query.data.startswith('back_menu'))
async def back_to_menu(callback_query):
    callback_message = callback_query.message
    await bot.edit_message_text(chat_id=callback_message.chat.id,message_id=callback_message.message_id,text="Выберите действие:",reply_markup=create_menu_markup())

def back_markup():
    delete_photo = [[InlineKeyboardButton(text='🔙Назад', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=delete_photo)

lock = asyncio.Lock()

@dp.callback_query_handler(lambda call: call.data == "back")
async def han_back(call):
    async with lock:
        if sent_messages_ids:
            last_message_id = sent_messages_ids[-1]
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=last_message_id)
            except exceptions.MessageToDeleteNotFound:
                await bot.send_message(call.message.chat.id, text='Произошла ошибка, в следствии чего фото не было удаленно, @mrstirlitz', parse_mode='html')
        await bot.send_message(chat_id=call.message.chat.id,text="О ком хотите узнать:",reply_markup=peples())

"""
Место для Бд
"""

try:
    with open("dbyl.py", "r") as handle:
        file_contents = handle.read()
        exec("database = " + file_contents)
except:
    database = {}

def add_user_to_db(user_id, username, user_name=None):
    if user_id not in database:
        database[user_id] = {
            'name': user_name,
            'user': username,
        }
        with open("dbyl.py", "w+") as handle:
            handle.write(str(database))

""""
Место для рассылки и просмотр бд
"""

@dp.message_handler(commands=['ras'])
async def ras(message):
    if message.from_user.id == admins:
        message_text = message.text.replace("/ras ", "")
        for user_id in database:
            try:
                await bot.send_message(user_id, message_text)
            except:
                await bot.send_message(chat_id=message.chat.id, text=f"Не удалось отправить сообщение пользователю с идентификатором: {user_id}")
    else:
        await bot.send_message(chat_id=message.chat.id, text="У вас нет прав на использование этой команды")

@dp.message_handler(commands=['msg'])
async def message_user(message):
    if message.from_user.id == admins:
        message_text = message.text.replace("/msg ", "")
        user_id = message_text.split(" ")[0]
        message_text = message_text.replace(user_id + " ", "")
        try:
            await bot.send_message(user_id, message_text)
            await bot.send_message(chat_id=message.chat.id, text=f"Сообщение отправлено пользователю с id: {user_id}")
        except:
            await bot.send_message(chat_id=message.chat.id, text=f"Не удалось отправить сообщение пользователю с идентификатором: {user_id}")

@dp.message_handler(commands=['help'])
async def admin_kb(message):
    if message.from_user.id == admins:
       await bot.send_message(chat_id=message.chat.id, text=f"Привет ВСЕМОГУЩИЙ {message.from_user.full_name}\n/see - Смотреть bd\n/ras <i>messege_text</i> - Отправить общюю рассылку \n/msg <i><b>id</b> message_text</i> - Отправить личное сообшение по id\nИ помни что каждый человек имнеет право быть услышанным!")


@dp.message_handler(commands=['see'])
async def see_user(message):
    if message.from_user.id == admins:
        if database:
            text = ""
            for user_id, user_data in database.items():
                text += f"ID: {user_id}\nUser: {user_data['user']}\nname: {user_data['name']}\n\n"
            await bot.send_message(chat_id=message.chat.id, text=text)
        else:
           await bot.send_message(chat_id=message.chat.id, text="Нечего нет")
    else:
        await bot.send_message(chat_id=message.chat.id, text="У вас нет прав на использование этой команды")

"""
Место для оброботки людей
"""

people_data = {
        "Дарья": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/dasha4.jpg',
            "caption": '''Привет!\nМоё имя Дарья, в основном меня зовут Даша, но те, кто давно в Young Life знают меня как Тут-турут 💁🏻‍♀(Да это отсылка к Даше путешественнице).\nЯ из Бишкека, но уже год живу в Караколе 💞, полюбила этот город. \nВ Young Life я с 2016г.\nЛюблю танцевать 💃🏻, думаю у меня хорошо получается (кхе-кхе 7 лет в танцах не прошли даром).Очень люблю петь 🎶 (3 года в музыкалке тоже не хухры-мухры 😌).\n🎲 Настольные игры - отдельный вид удовольствия.\nЛюблю ночные прогулки по городу 🌃,а еще смотреть фильмы и сериалы🍿.\nМечтаю стать фитнес-тренером 💪🏻.\nУ меня нет самой любимой песни 🤷🏻‍♀. Думаю могу рассказать ещё много всего, но уже при встрече 😉\nПриходи к нам на клуб💫'''
        },
        "Канат": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/pupkin.webp',
            "caption": '<b>Привет, меня зовут Канат! Я целеустремлённый! Умный! Самый хороший! Прекрасный! Просто красавчик. БОзар нэт мужЫк - в этом убеждена моя мама!!!</b>',
        },
        "Макс": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/sti.jpg',
            "caption": f'<i><span class="tg-spoiler">Это Макс и он создатель этого бота\n@MrStirlitz</span></i>',
            'has_spoilers': 'has_spoiler'
        },
        "София": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/sonia.jpg',
            "caption": '''Привет. Меня зовут София,\n(да, та что София прекрасная👸🏻😂 ), но все называют меня Соня , я люблю спать 🙃\nМне 16 лет.  Я учусь во 2 школе, работаю в кофейне, а ещё люблю лежать как овощ и ничего не делать🫠\nКак то в 2020 году , меня позвала подруга покушать бесплатно пиццу в young life, именно тогда меня и занесло сюда  😁 пицца уж очень вкусная была \nЯ люблю:\nПоэзию 🤓\nСлушать музыку 🎶\nИграть в настольные игры🎲\nКататься на скейте , коньках , сноуборде🛹⛸🏂\nГулять \nХодить в походы 🏕\nЛагеря young life 😍\nВкусную еду 😋\nИ ещё много всякого разного😌 \nПриходи к нам на клуб✨(у нас есть вкусняшки😂)'''
        },
        "Саида": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/saida.jpg',
            "caption": '''Привет!\nМеня зовут Саида.\nЯ в young Life не давно, но очень полюбила его. Young Life для меня стал семьёй.\nЯ с рождения живу в Караколе и очень люблю этот город.\nЛюблю заниматься спортом, читать и печь вкусную выпечку. Люблю проводить время с друзьями. Люблю гулять ночью, но родители не любят когда я гуляю поздно.\nЯ очень добрая и люблю людей.\nПриходи к нам на клуб и при встрече на клубе лучше познакомимся.'''
        },
        "Луиза": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/luiza.jpg',
            "caption": f'''Привет меня зовут Луиза, я лучшая в мире колонка. Я немного прихотлива, люблю работать только у истинных владельцев. А так обычно всегда с командой, я могу в любой момент помочь своим высококлассным звучанием!''',
        },
        "СФ-Даня": {
            "photo": 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/shaodwFiend.jpg',
            "caption": 'Самый лютый Shadow Fiend на районе, да еще и с арканой!',
        }
    }
sent_messages_ids = []
@dp.callback_query_handler(lambda call: True)
async def handle_callback(call):
    person = call.data
    await call.message.delete()
    data = people_data[person]
    if person == "Макс":
        sent_photo = await bot.send_photo(call.from_user.id, data["photo"], caption=data["caption"], parse_mode='HTML',
                                          reply_markup=back_markup(), has_spoiler=True)
    else:
        sent_photo = await bot.send_photo(call.from_user.id, data["photo"], caption=data["caption"], parse_mode='HTML',
                                          reply_markup=back_markup())
    sent_messages_ids.append(sent_photo.message_id)

@dp.message_handler(content_types=['text'])
async def secrets_text(message):
    print(message.from_user.first_name + '(' + str(message.from_user.id) + ") : " + message.text)
    if message.text.lower() == 'кто топ': await bot.send_message(message.chat.id,f'<i><span class="tg-spoiler">{message.from_user.first_name} Самый лучший, самый красивый, самый 😎z</span></i>', parse_mode='html')

if __name__ == '__main__':
    from aiogram import executor
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
