from sqlalchemy import Column, BigInteger, sql

from utils.db_api.db_gino import TimedBaseModel


class Love(TimedBaseModel):
    __tablename__ = 'love'
    liked = Column(BigInteger)
    likes = Column(BigInteger)

    query: sql.Select
    delete: sql.Delete
