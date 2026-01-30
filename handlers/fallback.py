from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from services.backend import ask_backend
from texts import ru, kg

router = Router()


@router.message()
async def fallback(message: Message, state: FSMContext):
    # ❌ если идёт FSM (онбординг) — НЕ ЛЕЗЕМ
    if await state.get_state() is not None:
        return

    data = await state.get_data()
    lang = data.get("language", "ru")
    texts = ru if lang == "ru" else kg

    # 1️⃣ дисклеймер показываем ОДИН РАЗ
    if not data.get("disclaimer_shown"):
        await state.update_data(disclaimer_shown=True)

        await message.answer(
            f"{texts.ASK_QUESTION}\n\n{texts.DISCLAIMER}"
        )
        return

    # 2️⃣ реальная обработка запроса
    user_text = (message.text or "").strip()

    if not user_text:
        await message.answer("Пожалуйста, напишите вопрос текстом.")
        return

    answer = await ask_backend(
        tg_id=message.from_user.id,
        text=user_text,
        language=lang,
    )

    await message.answer(answer)
