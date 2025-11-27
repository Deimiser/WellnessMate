from src.db.database import get_db
from src.db import crud
from sqlalchemy.orm import Session

def run_demo_pipeline():
    # Initialize DB session
    db: Session = next(get_db())

    # 1️⃣ Create a test user (or get existing)
    user = crud.get_user_by_name(db, name="Demo User")
    if not user:
        user = crud.create_user(
            db,
            name="Demo User",
            age=28,
            height=170.0,
            weight=65.0,
            preferences={"goal": "fitness", "reminders": True}
        )
        print(f"Created user: {user.name} (ID: {user.id})")
    else:
        print(f"User already exists: {user.name} (ID: {user.id})")

    # 2️⃣ Add a dummy daily log
    daily_data = {
        "steps": 8000,
        "sleep_hours": 7.0,
        "heart_rate_avg": 70,
        "extra_metrics": {"calories": 2100}
    }
    crud.add_daily_log(
        db,
        user_id=user.id,
        steps=daily_data["steps"],
        sleep_hours=daily_data["sleep_hours"],
        heart_rate_avg=daily_data["heart_rate_avg"],
        extra_metrics=daily_data["extra_metrics"]
    )
    print("Added daily log for demo user.")

    # 3️⃣ Add a dummy insight
    insights_text = "Keep up the good work! Try increasing daily steps to 8500."
    metrics = {"steps_trend": "up", "sleep_quality": "good"}
    crud.add_insight(db, user_id=user.id, insights_text=insights_text, metrics=metrics)
    print("Added sample insight.")

    # 4️⃣ Add a dummy wellness plan
    plan_text = "Walk 8500 steps tomorrow and aim for 7.5 hours of sleep."
    actions = {"steps_goal": 8500, "sleep_goal": 7.5}
    crud.add_wellness_plan(db, user_id=user.id, plan_text=plan_text, actions=actions)
    print("Added sample wellness plan.")

    # 5️⃣ Optional: add LLM session memory
    session_data = {
        "last_insights": insights_text,
        "last_plan": plan_text
    }
    crud.save_llm_memory(db, user_id=user.id, session_data=session_data)
    print("Saved demo LLM session memory.")

    print("\n✅ Demo pipeline executed successfully!")

if __name__ == "__main__":
    run_demo_pipeline()
