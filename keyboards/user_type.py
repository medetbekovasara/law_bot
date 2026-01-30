from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def user_type_kb(lang: str):
    buttons = {
        "ru": ["ИП", "ОсОО", "Физлицо", "Студент"],
        "kg": ["ЖИ", "ЖЧК", "Жеке адам", "Студент"],
    }

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=t, callback_data=f"user_type:{t}")]
            for t in buttons[lang]
        ]
    )
