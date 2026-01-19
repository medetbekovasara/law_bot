import httpx
from config import BACKEND_URL

async def create_or_update_user(payload: dict):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(f"{BACKEND_URL}/user", json=payload)
        r.raise_for_status()
        return r.json()

async def get_user(tg_id: int):
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(f"{BACKEND_URL}/user/{tg_id}")
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()
