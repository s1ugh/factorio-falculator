from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

class ItemModel(Base):
    __tablename__ = 'items'
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    stack_size: Mapped[str] = mapped_column(Integer, nullable=True)
    