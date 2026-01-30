from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.backend import send_user_data
from states.onboarding import OnboardingState
from texts import ru, kg

router = Router()

@router.message(OnboardingState.phone, F.contact)
async def phone_received(message: Message, state: FSMContext):
    data = await state.get_data()

    payload = {
        "tg_id": message.from_user.id,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
        "phone": message.contact.phone_number,
        "language": data["language"],
        "user_type": data["user_type"],
    }

    await send_user_data(payload)
    # await state.clear()