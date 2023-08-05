from sqlalchemy import Column, Integer, String
from database import Base, session


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=False, unique=False)
    username = Column(String, index=True, unique=True)
    language_code = Column(String, index=False, unique=False)
    is_bot = Column(String, index=True, unique=False)
    is_premium = Column(String, index=False, unique=False)
    first_name = Column(String, index=False, unique=False)
    last_name = Column(String, index=False, unique=False)
    link = Column(String, index=False, unique=False)
    external_id = Column(Integer, index=True, unique=True)


Base.metadata.create_all(session.bind)

