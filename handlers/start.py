from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.onboarding import OnboardingState
from keyboards.language import language_kb

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(OnboardingState.language)

    await message.answer(
        "Выберите язык / Тилди тандаңыз",
        reply_markup=language_kb()
    )
