import aiohttp
from config import BACKEND_URL
import logging


async def is_user_registered(tg_id: int) -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BACKEND_URL}/user/{tg_id}") as r:
            return r.status == 200

logger = logging.getLogger(__name__)


async def send_user_data(data: dict) -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{BACKEND_URL}/users",
                json=data,
                timeout=5,
            ) as r:
                if r.status in (200, 201):
                    return True

                text = await r.text()
                logger.error("Backend error %s: %s", r.status, text)
                return False

    except aiohttp.ClientError:
        logger.exception("Backend connection error")
        return False

async def ask_backend(tg_id: int, text: str, language: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{BACKEND_URL}/ask",
            json={
                "tg_id": tg_id,
                "question": text,
                "language": language,
            },
            timeout=60,
        ) as r:
            data = await r.json()
            return data.get("answer", "Не удалось получить ответ.")

