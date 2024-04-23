from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from bot.core.core import settings


class Database:
    def __init__(self):
        self.engine = create_async_engine(url='postgresql+asyncpg://test:root@localhost/image_bot', echo=True)
        self.session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db = Database()
