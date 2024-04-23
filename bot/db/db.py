from db_connect import db


async def get_db():
    async with db.session() as session:
        yield session
