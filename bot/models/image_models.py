from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from bot.db.base import Base


class BaseImage(Base):
    __tablename__ = 'images'

    image: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(server_default=func.now())
