from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import Onboarding
from keyboards import (
    language_keyboard,
    user_type_keyboard,
    phone_keyboard
)
from texts import TEXTS
from utils import t

router = Router()

@router.message(Onboarding.language)
async def choose_language(message: Message, state: FSMContext):
    if message.text == "Русский":
        lang = "ru"
    elif message.text == "Кыргызча":
        lang = "kg"
    else:
        await message.answer("Тилди кнопка менен тандаңыз / Выберите язык кнопкой.")
        return

    await state.update_data(language=lang)
    await state.set_state(Onboarding.user_type)

    await message.answer(
        t(lang, "choose_user_type"),
        reply_markup=user_type_keyboard(lang)
    )


@router.message(Onboarding.user_type)
async def choose_user_type(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data["language"]

    valid_types = {
        "ru": ["ИП", "ОсОО", "Физическое лицо", "Студент-юрист"],
        "kg": ["Жеке ишкер", "ОсОО", "Жеке адам", "Юрист-студент"]
    }

    if message.text not in valid_types[lang]:
        await message.answer(t(lang, "choose_user_type"))
        return

    await state.update_data(user_type=message.text)
    await state.set_state(Onboarding.first_name)

    await message.answer(t(lang, "enter_first_name"))


@router.message(Onboarding.first_name)
async def first_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data["language"]

    await state.update_data(first_name=message.text)
    await state.set_state(Onboarding.last_name)

    await message.answer(t(lang, "enter_last_name"))


@router.message(Onboarding.last_name)
async def last_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data["language"]

    await state.update_data(last_name=message.text)
    await state.set_state(Onboarding.phone)

    await message.answer(
        t(lang, "send_phone"),
        reply_markup=phone_keyboard()
    )


@router.message(Onboarding.phone)
async def phone(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data["language"]

    if not message.contact:
        await message.answer(t(lang, "send_phone"))
        return

    phone_number = message.contact.phone_number

    user_payload = {
        "tg_id": message.from_user.id,
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "username": message.from_user.username,
        "phone": phone_number,
        "language": lang,
        "user_type": data["user_type"],
    }

    # TODO: здесь будет вызов backend
    # await create_user(user_payload)

    await state.clear()

    await message.answer(
        t(lang, "onboarding_done"),
        reply_markup=None
    )
