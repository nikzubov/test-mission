import logging

import aiohttp


class APIClient:
    headers = headers = {"Content-Type": "application/json"}

    async def get_query(self, url, prompt=None):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    url=url,
                    headers=self.headers,
                    json=prompt,
                ) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data
            except aiohttp.ClientError as e:
                logging.error(e)
            return 'Произошла ошибка'

    async def post_query(self, url, prompt):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    url=url,
                    headers=self.headers,
                    json=prompt
                ) as response:
                    response.raise_for_status()
                    data = await response.text()
                    return data
            except aiohttp.ClientError as e:
                logging.error(e)
            return 'Произошла ошибка'


api_client = APIClient()
