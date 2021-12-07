import telebot
import config

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('2130619696:AAEyHVjqm-T-_OKnXfx-kBiRzBBkZRva4Dw')

INSTA = 'https://www.instagram.com/why_violetta/'

report = {}

report_text = {
    "place_hand": "Рука",
    "place_leg": "Нога",
    "place_back": "Спина",
    "place_ribs": "Рёбра",
    "place_clavicle":"Ключицы",
    "place_buttock": "Ягодицы",
    "start_place_no": "Пока не знаю",
    "place_no_visible_hand": "Кисть руки",
    "place_no_visible_wrist": "Запястье",
    "place_no_visible_forearm": "Предплечье",
    "place_no_visible_shoulder": "Плечо",
    "place_no_visible_hip": "Бедро",
    "place_no_visible_shin": "Голень",
    "place_no_visible_neck": "Шея",
    "place_no_visible_clavicle": "Ключица",
    "place_no_invisible_back": "Спина",
    "place_no_invisible_ribs": "Рёбра",
    "place_no_invisible_chest": "Грудь",
    "place_no_invisible_buttock": "Ягодицы",
    "place_no_invisible_foot": "Стопа",
    "color_color": "Цветная",
    "color_black": "Чёрная",
    "size_small": "Совсем маленькую, до 5см",
    "size_medium": "В пределах альбомного листа",
    "size_large": "Хочу масштабную, рукав или на всю спину, например",
    "method_vk": "vk",
    "method_tg": "Telegram",
    "method_wa": "WhatsApp",
    "method_ig": "Instagram",
    "method_lvs": "Лично в студии",
    "sketch_yes": "Да",
    "sketch_no": "Нет",
}


@bot.message_handler(commands=["start"])
def command_start(message):
    chat_id = message.chat.id
    report[chat_id] = {}
    report[chat_id]["Telegram username"] = f"@{message.from_user.username}"
    report[chat_id]["Telegram ID"] = message.from_user.id

    # sti = open('AnimatedSticker.tgs', 'rb')
    # bot.send_sticker(message.chat.id, sti)

    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton("Давай!", callback_data="start")
    markup.add(item1)

    m = "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>!" \
        " Давай я помогу тебе подобрать идеальную татуировку)"
    bot.send_message(chat_id, m.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "start":
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Да", callback_data="start_yes")
        item2 = InlineKeyboardButton("Я просто посмотреть 👀", callback_data="start_just_see")
        item3 = InlineKeyboardButton("Нет", callback_data="start_no")
        markup.add(item1, item2, item3)

        bot.send_message(chat_id, 'Ты точно хочешь татуировку?', reply_markup=markup)
    elif call.data == "start_yes":
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Рука", callback_data="place_hand")
        item2 = InlineKeyboardButton("Нога", callback_data="place_leg")
        item3 = InlineKeyboardButton("Спина", callback_data="place_back")
        item4 = InlineKeyboardButton("Рёбра", callback_data="place_ribs")
        item5 = InlineKeyboardButton("Ключицы", callback_data="place_clavicle")
        item6 = InlineKeyboardButton("Ягодицы", callback_data="place_buttock")
        item7 = InlineKeyboardButton("Пока не знаю", callback_data="start_place_no")
        markup.add(item1, item2, item3, item4, item5, item6, item7)

        bot.send_message(chat_id, 'Ты уже знаешь, на каком месте она будет?', reply_markup=markup)
    elif call.data == 'start_just_see':
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Instagram", url=INSTA)
        markup.add(item1)
        bot.send_message(chat_id, 'Тогда предлагаю тебе глянуть на мой аккаунт в инсте,' +
                         ' уверена ты найдёшь что-то для себя 🤗', reply_markup=markup)
    elif call.data == "start_no":
        bot.send_message(chat_id, 'Поздравляю, тебе не нужна татуировка, хорошего тебе дня)')
    elif call.data == "start_place_no":
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Ага", callback_data="start_place_no_visible")
        item2 = InlineKeyboardButton("Неа", callback_data="start_place_no_invisible")
        markup.add(item1, item2)

        bot.send_message(chat_id, 'Хочешь, чтобы татуировка была на видном месте?', reply_markup=markup)
    elif call.data == "start_place_no_visible":
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Кисть руки", callback_data="place_no_visible_hand")
        item2 = InlineKeyboardButton("Запястье", callback_data="place_no_visible_wrist")
        item3 = InlineKeyboardButton("Предплечье", callback_data="place_no_visible_forearm")
        item4 = InlineKeyboardButton("Плечо", callback_data="place_no_visible_shoulder")
        item5 = InlineKeyboardButton("Бедро", callback_data="place_no_visible_hip")
        item6 = InlineKeyboardButton("Голень", callback_data="place_no_visible_shin")
        item7 = InlineKeyboardButton("Шея", callback_data="place_no_visible_neck")
        item8 = InlineKeyboardButton("Ключица", callback_data="place_no_visible_clavicle")
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

        bot.send_message(chat_id, "Где именно?", reply_markup=markup)
    elif call.data == "start_place_no_invisible":
        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Спина", callback_data="place_no_invisible_back")
        item2 = InlineKeyboardButton("Рёбра", callback_data="place_no_invisible_ribs")
        item3 = InlineKeyboardButton("Грудь", callback_data="place_no_invisible_chest")
        item4 = InlineKeyboardButton("Ягодицы", callback_data="place_no_invisible_buttock")
        item5 = InlineKeyboardButton("Стопа", callback_data="place_no_invisible_foot")
        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(chat_id, "Где конкретно?", reply_markup=markup)
    elif call.data.startswith("place_"):
        report[chat_id]['Место'] = call.data

        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Цветная", callback_data="color_color")
        item2 = InlineKeyboardButton("Чёрная", callback_data="color_black")
        markup.add(item1, item2)

        bot.send_message(chat_id, 'Ты хочешь цветную или чёрную?', reply_markup=markup)
    elif call.data.startswith("color_"):
        report[chat_id]['Цвет'] = call.data

        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Совсем маленькую, до 5см", callback_data="size_small")
        item2 = InlineKeyboardButton("В пределах альбомного листа", callback_data="size_medium")
        item3 = InlineKeyboardButton("Хочу масштабную, рукав или на всю спину, например", callback_data="size_large")
        markup.add(item1, item2, item3)

        bot.send_message(chat_id, 'А какого примерно размера?', reply_markup=markup)
    elif call.data.startswith("size_"):
        report[chat_id]['Размер'] = call.data

        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("Ага, хочу обсудить", callback_data="sketch_yes")
        item2 = InlineKeyboardButton("Нет, мне нужна с этим помощь", callback_data="sketch_no")
        markup.add(item1, item2)

        bot.send_message(chat_id, 'Хорошо, у тебя уже есть идея или примеры татуировок/рисунков,' +
                         ' которые тебе нравятся?', reply_markup=markup)
    elif call.data.startswith("sketch_"):
        report[chat_id]['Эскиз'] = call.data

        bot.send_message(chat_id, 'Отлично, как я могу к тебе обращаться?')
    elif call.data.startswith("method_"):
        report[chat_id]['Способ связи'] = call.data
        bot.send_message(chat_id, 'Оставьте контакт')

       #свежее
    # elif bot.answer_callback_query(callback_query_id=cmd.id, text="Неверно, Верный ответ...", show_alert=True)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    chat_id = message.chat.id

    if "Способ связи" in report[chat_id]:
        report[chat_id]['Контакт'] = message.text

        bot.send_message(-687551222, convert_report(report[chat_id]))
        bot.send_message(chat_id, 'Спасибо! Я свяжусь с тобой в ближайшее время)')
    elif "Размер" in report[chat_id]:
        report[chat_id]['Имя клиента'] = message.text

        markup = InlineKeyboardMarkup(row_width=1)
        item1 = InlineKeyboardButton("vk", callback_data="method_vk")
        item2 = InlineKeyboardButton("Telegram", callback_data="method_tg")
        item3 = InlineKeyboardButton("WhatsApp", callback_data="method_wa")
        item4 = InlineKeyboardButton("Instagram", callback_data="method_ig")
        item5 = InlineKeyboardButton("Лично в студии", callback_data="method_lvs")
        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(chat_id, 'Приятно познакомиться) Спасибо за прохождение теста, ' +
                         'надеюсь, тебе теперь стало понятнее, какая татуировка лично для тебя ' +
                         'будет идеальна. Чтобы стало ещё проще, предлагаю продолжить общение на' +
                         ' консультации в переписке в любом удобном для тебя мессенджере или можем' +
                         ' встретиться на консультации в студии. Какой вариант тебе комфортнее:',
                         reply_markup=markup)


def convert_report(r):
    text = "Анкета\n"

    for key in r:
        val = r[key]
        if val in report_text:
            text += f'{key}: {report_text[val]}\n'
        else:
            text += f'{key}: {val}\n'

    return text


bot.polling(none_stop=True, interval=0)

# Нужна обработка исключений:
# при попытке отправить анкету в чат для анкет: если бота нет в чате - вылетает ошибка.

# Если пользователь пытается отправить сообщение в чат вместо нажатия кнопки

# Возможно, по окончании анкетирования стоит добавить кнопку, "заполнить заново"


# bot.answer_callback_query(callback_query_id=cmd.id, text="Изменять голос запрещено", show_alert=False)
#
# bot.answer_callback_query(callback_query_id=cmd.id, text="Неверно, Верный ответ...", show_alert=True)