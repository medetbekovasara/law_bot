from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from states import Onboarding
from keyboards import language_keyboard
from api import get_user

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)

    if user and user.get("onboarding_completed"):
        await message.answer("Бот в разработке. Скоро будет доступен функционал ⚙️")
        return

    await state.set_state(Onboarding.language)
    await message.answer(
        "Выберите язык:",
        reply_markup=language_keyboard()
    )
