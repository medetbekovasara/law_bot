from aiogram import Dispatcher

from handlers.start import router as start_router
from handlers.fallback import router as fallback_router
from handlers.onboarding.language import router as onboarding_language
from handlers.onboarding.user_type import router as onboarding_user_type
from handlers.onboarding.phone import router as onboarding_phone

def setup_routers(dp):
    dp.include_router(start_router)
    dp.include_router(onboarding_language)
    dp.include_router(onboarding_user_type)
    dp.include_router(onboarding_phone)
    dp.include_router(fallback_router)
