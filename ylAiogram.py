# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '5589637928:AAG4Ell_L2GAFR7hHg6VQGrcoT6uV_q3BGk'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
admins = 1138500722

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEHaNdjz6fTiPMZUhWcdBH0dGvKaHydMAACWiMAAv8a8UkmXuJEEdR7iy0E')
    await bot.send_message(message.chat.id, f'Привет, <b><u>{message.from_user.first_name}</u> Чтобы узнать о людях в Young Life /yl</b>', parse_mode='html')



@dp.message_handler(commands=['help'])
async def comands(message):
    await bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEHaNVjz6fRmbt-lTSlPAZwQ7bvyyWsyAACsigAAknB6UkXARmOdy0XEC0E'), \
        await bot.send_message(message.chat.id, '''Все возможные команды:\n/yl\n/info\n/insta\nСпасибо за понимание!''')

@dp.message_handler(commands=['info'])
async def info(message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHaM9jz6cFFFg_qVJIh2wLdDLnJYn15AACJiQAAtab6EkBLpFvk5TKwy0E')
    await bot.send_message(message.chat.id, f'<i><span class="tg-spoiler">Young Life - это место, где тебя ждут, место где тебя ценят и место где тебе не будет скучно!\n\nМы те, кто организовывает разнообразные увлекательные мероприятия для молодёжи и подростков! Квесты, лагеря, сумашедшие вечера и это ещё не всё!\n\nYoung Life - это там, где тебя поймут и выслушают, место встречи друзей, хорошее общение и просто там, где можно отлично провести время в хорошей компании за чашкой чая или миской поп-корна смотря фильм.\n\nРазные интересные и захватывающие настольные игры и другие разнообразные виды времяпрепровождения не дадут тебе скучать!</span></i>', parse_mode='html')


@dp.message_handler(commands=['insta'])
async def see_insta(message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHaNFjz6fKWu6ceR3xJXyOAwpq9JNJlwACCyYAAnvf6EkyzhxMlzZi-S0E')
    marrup = InlineKeyboardMarkup()
    marrup.add(InlineKeyboardButton('Открыть Инсту', url='https://www.instagram.com/yl_karakol/'))
    await bot.send_message(message.chat.id, 'Наш Инстаграм!!!', reply_markup=marrup)


try:
    with open("dbyl.py", "r") as handle:
        file_contents = handle.read()
        exec("database = " + file_contents)
except:
    database = {}

@dp.message_handler(commands=['yl'])
async def leder_helpers(message):
    user_id = message.from_user.id
    username = message.from_user.username
    user_name = message.from_user.first_name
    add_user_to_db(user_id, username, user_name)
    await bot.send_message(message.chat.id, '<u>Сейчас я расскажу о команде Young life Karakol</u>', parse_mode='html'),\
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHaNNjz6fNgCKO1lJquLojxaswZ_-xNwACxiAAAlIX6Emi2MpPVYk8qy0E')
    markup = InlineKeyboardMarkup()
    leaders_button = InlineKeyboardButton("Лидеры", callback_data="Лидеры")
    helpers_button = InlineKeyboardButton("Помощники", callback_data="Помощники")
    markup.row(leaders_button, helpers_button)
    await bot.send_message(message.chat.id, "О ком хочешь узнать:", reply_markup=markup)

people = []

@dp.callback_query_handler(lambda call: call.data == "◀Назад" or call.data == "back")
async def han_back(call):
    if call.data == '◀Назад':
        markup = InlineKeyboardMarkup()
        leaders_button = InlineKeyboardButton("Лидеры", callback_data="Лидеры")
        helpers_button = InlineKeyboardButton("Помощники", callback_data="Помощники")
        markup.row(leaders_button, helpers_button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="О ком хочешь узнать:",reply_markup=markup)
    elif sent_messages_ids:
        last_message_id = sent_messages_ids.pop()
        await bot.delete_message(chat_id=call.message.chat.id, message_id=last_message_id)



sent_messages_ids = []
back_button = types.InlineKeyboardButton('◀Назад', callback_data='back')
keyboard = types.InlineKeyboardMarkup().add(back_button)




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


def add_user_to_db(user_id, username, user_name=None):
    if user_id not in database:
        database[user_id] = {
            'name': user_name,
            'user': username,
        }
        with open("dbyl.py", "w+") as handle:
            handle.write(str(database))


@dp.message_handler(commands=['pip'])
async def ras(message):
    if message.from_user.id == admins:
        message_text = message.text.replace("/pip ", "")
        for user_id in database:
            try:
                await bot.send_message(user_id, message_text)
            except:
                await bot.send_message(chat_id=message.chat.id, text=f"Не удалось отправить сообщение пользователю с идентификатором: {user_id}")
    else:
        await bot.send_message(chat_id=message.chat.id, text="У вас нет прав на использование этой команды")

@dp.message_handler(commands=['pi'])
async def message_user(message):
    if message.from_user.id == admins:
        message_text = message.text.replace("/pi ", "")
        user_id = message_text.split(" ")[0]
        message_text = message_text.replace(user_id + " ", "")
        try:
            await bot.send_message(user_id, message_text)
            await bot.send_message(chat_id=message.chat.id, text=f"Сообщение отправлено пользователю с id: {user_id}")
        except:
            await bot.send_message(chat_id=message.chat.id, text=f"Не удалось отправить сообщение пользователю с идентификатором: {user_id}")
    else:
        await bot.send_message(chat_id=message.chat.id, text="У вас нет прав на использование этой команды")



@dp.callback_query_handler(lambda call: True)
async def handle_callback(call):
    if call.data == "Лидеры":
        leaders = []
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton('Дарья', callback_data='Дарья'))
        markup.row(InlineKeyboardButton('Канат', callback_data='Канат'))
        markup.row(InlineKeyboardButton('София', callback_data='София'))
        markup.row(InlineKeyboardButton('Саида', callback_data='Саида'))
        markup.row(InlineKeyboardButton('Луиза', callback_data='Луиза'))
        for leader in leaders:
            button = InlineKeyboardButton(leader, callback_data="Лидеры")
            markup.add(button)
        back_button = InlineKeyboardButton("◀Назад", callback_data="◀Назад")
        markup.add(back_button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лидеры:",
                              reply_markup=markup)
    elif call.data == "Помощники":
        helpers = []
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton('Элиза', callback_data='Элиза'))
        markup.row(InlineKeyboardButton('Макс', callback_data='Макс'))

        for helper in helpers:
            button = InlineKeyboardButton(helper, callback_data="Помощник")
            markup.add(button)
        back_button = InlineKeyboardButton("◀Назад", callback_data="◀Назад")
        markup.add(back_button)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Помощники:",
                              reply_markup=markup)

    if call.data == "Дарья":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/dasha4.jpg', caption='''Привет!
Моё имя Дарья, в основном меня зовут Даша, но те, кто давно в Young Life знают меня как Тут-турут 💁🏻‍♀(Да это отсылка к Даше путешественнице).
Я из Бишкека, но уже год живу в Караколе 💞, полюбила этот город. 
В Young Life я с 2016г.
Люблю танцевать 💃🏻, думаю у меня хорошо получается (кхе-кхе 7 лет в танцах не прошли даром).Очень люблю петь 🎶 (3 года в музыкалке тоже не хухры-мухры 😌).
🎲 Настольные игры - отдельный вид удовольствия.
Люблю ночные прогулки по городу 🌃,а еще смотреть фильмы и сериалы🍿.
Мечтаю стать фитнес-тренером 💪🏻.
У меня нет самой любимой песни 🤷🏻‍♀. Думаю могу рассказать ещё много всего, но уже при встрече 😉
Приходи к нам на клуб💫''', reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)
    elif call.data == "Канат":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/pupkin.webp',
                                    caption='<b>Привет, меня зовут Канат! Я целеустремлённый! Умный! Самый хороший! Прекрасный! Просто красавчик. БОзар нэт мужЫк - в этом убеждена моя мама!!!</b>',
                                    parse_mode='html',
                                    reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)

    elif call.data == "Макс":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/sti.jpg',
                                    caption=f'<i><span class="tg-spoiler">Это Макс и он создатель этого бота\n@MrStirlitz</span></i>',
                                    parse_mode='html', reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)

    elif call.data == "София":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/sonia.jpg',
                                    caption='''Привет. Меня зовут София,
(да, та что София прекрасная👸🏻😂 ), но все называют меня Соня , я люблю спать 🙃
Мне 16 лет.  Я учусь во 2 школе, работаю в кофейне, а ещё люблю лежать как овощ и ничего не делать🫠
Как то в 2020 году , меня позвала подруга покушать бесплатно пиццу в young life, именно тогда меня и занесло сюда  😁 пицца уж очень вкусная была 
Я люблю:
Поэзию 🤓
Слушать музыку 🎶
Играть в настольные игры🎲
Кататься на скейте , коньках , сноуборде🛹⛸🏂
Гулять 
Ходить в походы 🏕
Лагеря young life 😍
Вкусную еду 😋
И ещё много всякого разного😌 
Приходи к нам на клуб✨(у нас есть вкусняшки😂)''', reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)

    elif call.data == "Саида":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/saida.jpg',
                                    caption='''Привет!
Меня зовут Саида.
Я в young Life не давно, но очень полюбила его. Young Life для меня стал семьёй.
Я с рождения живу в Караколе и очень люблю этот город.
Люблю заниматься спортом, читать и печь вкусную выпечку. Люблю проводить время с друзьями. Люблю гулять ночью, но родители не любят когда я гуляю поздно.
Я очень добрая и люблю людей.
Приходи к нам на клуб и при встрече на клубе лучше познакомимся.''',
                                    reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)

    elif call.data == "Элиза":
        sent_photo = await bot.send_photo(call.from_user.id, 'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/iliza.jpg',
                                    caption='''привет.
меня зовут элиза.
и я подросток с Каракола, для которого young life стал очень важной и любимой частичкой души.
так же, я самый младший участник в young life, но не смотря на это я преобладаю достаточно взрослым умом и в целом я очень интересная личность.
я люблю читать книги.умею правильно расставлять приоритеты и размышлять.со мной легко найти общий язык.сама по себе являюсь очень сильной, но одновременно очень ранимой личностью.я очень позитивная, эмоциональная, амбициозная и очень талантливая.я очень боюсь животных, даже кошек (простите).
ENTP - мой тип личности, да я полемист.любимый жанр музыки : фонк и классическая музыка.
для меня young life - это не место, а люди и неимоверный комфорт. благодоря yl я вышла из зоны комфорта и не боюсь быть собой. уже как год как я частичка yl.для меня это что-то очень важное, и то что я очень люблю и ценю.
—ƍʎvʞ ɐн wɐн ʞ иɓохиdu.''', reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)

    elif call.data == "Луиза":
        sent_photo = await bot.send_photo(call.from_user.id,
                                    'https://d8d3741a-85ae-44d9-9864-dbd58cfd39c9.id.repl.co/luiza.jpg',
                                    caption='''Привет меня зовут Луиза, я лучшая в мире колонка. Я немного прихотлива, люблю работать только у истинных владельцев. А так обычно всегда с командой, я могу в любой момент помочь своим высококлассным звучанием!''',
                                    reply_markup=keyboard)
        sent_messages_ids.append(sent_photo.message_id)
@dp.message_handler(content_types=['text'])
async def secrets_text(message):
    if message.text.lower() == 'кто топ':
        await bot.send_message(message.chat.id,f'<i><span class="tg-spoiler">{message.from_user.first_name} Самый лучший, самый красивый, самый 😎z</span></i>', parse_mode='html')
from sys import exit
@dp.message_handler(commands=["exit"])
async def exit_system(msg):
 if msg.from_user.id==2028784660:
  await bot.send_message(msg.chat.id,"bot off")
  dp.stop_polling()
  await dp.wait_closed()
  exit(0)
if __name__ == '__main__':
    executor.start_polling(dp)