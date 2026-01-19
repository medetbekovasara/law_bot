from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Русский"), KeyboardButton(text="Кыргызча")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

def user_type_keyboard(lang: str):
    if lang == "kg":
        buttons = ["Жеке ишкер", "ОсОО", "Жеке адам", "Юрист-студент"]
    else:
        buttons = ["ИП", "ОсОО", "Физическое лицо", "Студент-юрист"]

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b)] for b in buttons],
        resize_keyboard=True
    )

def phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Отправить номер", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
