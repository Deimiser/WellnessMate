# src/db/crud.py

from sqlalchemy.orm import Session
from datetime import date, datetime
from . import models

# ======================================================
# USERS
# ======================================================

def create_user(db: Session, name: str, age: int, height: float, weight: float, preferences: dict):
    user = models.User(
        name=name,
        age=age,
        height=height,
        weight=weight,
        preferences=preferences
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    """Required for demo_pipeline.py"""
    return db.query(models.User).filter(models.User.name == name).first()


# ======================================================
# DAILY LOGS
# ======================================================

def add_daily_log(db: Session, user_id: int, steps: int, sleep_hours: float, heart_rate_avg: float, extra_metrics: dict):
    log = models.DailyLog(
        user_id=user_id,
        date=date.today(),
        steps=steps,
        sleep_hours=sleep_hours,
        heart_rate_avg=heart_rate_avg,
        extra_metrics=extra_metrics
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_daily_logs(db: Session, user_id: int):
    return db.query(models.DailyLog).filter(models.DailyLog.user_id == user_id).all()


# ======================================================
# INSIGHTS
# ======================================================

def add_insight(db: Session, user_id: int, insights_text: str, metrics: dict):
    insight = models.Insight(
        user_id=user_id,
        date=date.today(),
        insights_text=insights_text,
        metrics=metrics
    )
    db.add(insight)
    db.commit()
    db.refresh(insight)
    return insight


# ======================================================
# WELLNESS PLANS
# ======================================================

def add_wellness_plan(db: Session, user_id: int, plan_text: str, actions: dict):
    plan = models.WellnessPlan(
        user_id=user_id,
        date=date.today(),
        plan_text=plan_text,
        actions=actions
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


# ======================================================
# LLM MEMORY
# ======================================================

def save_llm_memory(db: Session, user_id: int, session_data: dict):
    memory = db.query(models.LLMMemory).filter(models.LLMMemory.user_id == user_id).first()

    if memory:
        memory.session_data = session_data
        memory.last_updated = datetime.now()
    else:
        memory = models.LLMMemory(
            user_id=user_id,
            session_data=session_data,
            last_updated=datetime.now()
        )
        db.add(memory)

    db.commit()
    db.refresh(memory)
    return memory
