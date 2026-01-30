from aiogram.fsm.state import StatesGroup, State


class OnboardingState(StatesGroup):
    language = State()
    user_type = State()
    phone = State()
