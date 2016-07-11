from sqlalchemy import Column, Integer, String
from database import Base

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    text = Column(String(160))

    def __repr__(self):
        return "<Tweet '%r'>" % (self.text)