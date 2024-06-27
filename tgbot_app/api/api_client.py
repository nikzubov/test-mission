import logging

import aiohttp


class APIClient:

    async def get_query(self, headers, prompt=None):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    self.url,
                    headers=headers,
                    json=prompt,
                ) as response:
                    response.raise_for_status()
                    data = await response.text()
                    return data
            except aiohttp.ClientError as e:
                logging.error(e)
            return 'Произошла ошибка'
    
    async def post_query(self, headers, prompt):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    self.url,
                    headers=headers,
                    json=prompt
                ) as response:
                    response.raise_for_status()
                    data = await response.text()
                    return data
            except aiohttp.ClientError as e:
                logging.error(e)
            return 'Произошла ошибка'


api_client = APIClient()
