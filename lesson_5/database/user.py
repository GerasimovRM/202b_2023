from sqlalchemy import Column, Integer, String

from database.base_meta import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
