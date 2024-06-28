from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from config import settings

URL = f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@db:5432/{settings.POSTGRES_DB}'


class DataBase:
    def __init__(self, url, pool_size=5):
        self.engine = create_async_engine(
            url=url,
            echo=True,
            pool_size=pool_size
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            expire_on_commit=False
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            yield session

    async def create_db(self, base):
        async with self.engine.begin() as conn:
            await conn.run_sync(base.metadata.create_all)

    async def drop_db(self, base):
        async with self.engine.begin() as conn:
            await conn.run_sync(base.metadata.drop_all)


database = DataBase(url=URL)
