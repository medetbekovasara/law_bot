from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states.onboarding import OnboardingState
from keyboards.contact import contact_kb
from texts import ru, kg

router = Router()


@router.callback_query(OnboardingState.user_type, F.data.startswith("user_type:"))
async def user_type_selected(call: CallbackQuery, state: FSMContext):
    user_type = call.data.split(":")[1]

    data = await state.get_data()
    lang = data["language"]

    await state.update_data(user_type=user_type)
    await state.set_state(OnboardingState.phone)

    text = ru.SEND_PHONE if lang == "ru" else kg.SEND_PHONE

    await call.message.answer(text, reply_markup=contact_kb())
    await call.answer()
