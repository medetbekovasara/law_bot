from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def language_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
                InlineKeyboardButton(text="🇰🇬 Кыргызча", callback_data="lang_kg"),
            ]
        ]
    )
