# src/db/models.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    preferences = Column(JSON)

    daily_logs = relationship("DailyLog", back_populates="user")
    insights = relationship("Insight", back_populates="user")
    wellness_plans = relationship("WellnessPlan", back_populates="user")
    llm_memory = relationship("LLMMemory", back_populates="user")


class DailyLog(Base):
    __tablename__ = "daily_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    steps = Column(Integer)
    sleep_hours = Column(Float)
    heart_rate_avg = Column(Float)
    extra_metrics = Column(JSON)

    user = relationship("User", back_populates="daily_logs")


class Insight(Base):
    __tablename__ = "insights"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    insights_text = Column(Text)
    metrics = Column(JSON)

    user = relationship("User", back_populates="insights")


class WellnessPlan(Base):
    __tablename__ = "wellness_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    plan_text = Column(Text)
    actions = Column(JSON)

    user = relationship("User", back_populates="wellness_plans")


class LLMMemory(Base):
    __tablename__ = "llm_memory"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_data = Column(JSON)
    last_updated = Column(Date)

    user = relationship("User", back_populates="llm_memory")
