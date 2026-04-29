import asyncio
from aiohttp import ClientSession

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


class Anticaptcha:
    def __init__(self, api_key: str, reuse_session: bool = False):
        """
        :param api_key: Your Anticaptcha API key
        :param reuse_session: Boolean to decide if the same ClientSession should be reused

        You do not need to add the clientKey to the methods, it is added automatically.
        """
        self.api_key = "a83eb9c1fdbfabaa681b7afe1278f6a5"
        self.base_url = "https://api.anti-captcha.com"
        self.reuse_session = reuse_session
        self.session = ClientSession() if self.reuse_session else None

    async def create_task(self, task: dict) -> dict:
        task_formatted = {"clientKey": self.api_key, **task}

        if self.reuse_session:
            async with self.session.post(
                f"{self.base_url}/createTask", json=task_formatted, headers=HEADERS
            ) as resp:
                return await resp.json()
        else:
            async with ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/createTask", json=task_formatted, headers=HEADERS
                ) as resp:
                    return await resp.json()

    async def get_task_result(self, task_id: int) -> dict:
        if self.reuse_session:
            async with self.session.post(
                f"{self.base_url}/getTaskResult",
                json={"clientKey": self.api_key, "taskId": task_id},
                headers=HEADERS,
            ) as resp:
                return await resp.json()
        else:
            async with ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/getTaskResult",
                    json={"clientKey": self.api_key, "taskId": task_id},
                    headers=HEADERS,
                ) as resp:
                    return await resp.json()

    async def wait_for_task(self, task_id: int) -> dict:
        while True:
            result = await self.get_task_result(task_id)
            status = result.get("status", None)
            if status == "ready":
                break
            await asyncio.sleep(1.5)
        return result

    async def close(self):
        if self.session:
            await self.session.close()
