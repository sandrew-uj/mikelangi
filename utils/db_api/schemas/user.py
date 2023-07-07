from sqlalchemy import Column, BigInteger, String, sql, LargeBinary, Integer

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    description = Column(String(255))
    gender = Column(String(100))
    interest = Column(String(10))
    image = Column(LargeBinary(100))

    referral = Column(BigInteger)

    query: sql.Select
