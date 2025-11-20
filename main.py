from dotenv import load_dotenv
load_dotenv()

from src.agents.data_agent import DataAgent
from src.agents_llm.llm_planner_agent import LLMPlannerAgent


def run_pipeline():
    # Data agent — same as before
    data_agent = DataAgent(mode="dataset")
    df = data_agent.get_data("data/raw/fitbit.csv")

    # Convert df to dictionary for LLM-safe serialization
    stats = df.to_dict()

    # Planner agent orchestrates the workflow
    planner = LLMPlannerAgent()
    result = planner.run(stats)

    insights = result["insights"]
    plan = result["plan"]

    print("\n=== INSIGHTS ===")
    print(insights)

    print("\n=== DAILY PLAN ===")
    print(plan)


if __name__ == "__main__":
    run_pipeline()
