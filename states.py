from aiogram.fsm.state import State, StatesGroup

class Onboarding(StatesGroup):
    language = State()
    user_type = State()
    first_name = State()
    last_name = State()
    phone = State()
