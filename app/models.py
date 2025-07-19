# Database models
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    salary = Column(String, nullable=True)
    link = Column(String, unique=True)
    posted_date = Column(DateTime, default=datetime.utcnow)
