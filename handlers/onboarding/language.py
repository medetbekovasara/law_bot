from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states.onboarding import OnboardingState
from keyboards.user_type import user_type_kb
from texts import ru, kg

router = Router()


@router.callback_query(OnboardingState.language, F.data.startswith("lang_"))
async def language_selected(call: CallbackQuery, state: FSMContext):
    lang = call.data.split("_")[1]

    await state.update_data(language=lang)
    await state.set_state(OnboardingState.user_type)

    text = ru.SELECT_USER_TYPE if lang == "ru" else kg.SELECT_USER_TYPE

    await call.message.answer(text, reply_markup=user_type_kb(lang))
    await call.answer()
