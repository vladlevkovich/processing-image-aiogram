from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from bot.db.base import Base
# from bot.db.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(unique=True, index=True)
    username: Mapped[str] = mapped_column(nullable=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now())

