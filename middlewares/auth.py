from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from services.backend import is_user_registered
from states.onboarding import OnboardingState


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        # 1. Безопасно получаем пользователя
        if isinstance(event, Message):
            user = event.from_user

            # ✅ ВСЕГДА пропускаем /start
            if event.text and event.text.startswith("/start"):
                return await handler(event, data)

        elif isinstance(event, CallbackQuery):
            user = event.from_user
        else:
            return await handler(event, data)

        state: FSMContext = data.get("state")

        # 2. Если пользователь в процессе онбординга — не мешаем
        if state:
            current = await state.get_state()
            if current and current.startswith(OnboardingState.__name__):
                return await handler(event, data)

        # 3. Проверка регистрации
        if not await is_user_registered(user.id):
            if isinstance(event, Message):
                await event.answer("Сначала пройди регистрацию через /start")
            elif isinstance(event, CallbackQuery):
                await event.message.answer("Сначала пройди регистрацию через /start")
                await event.answer()

            return  # ⛔ стоп обработка

        return await handler(event, data)
