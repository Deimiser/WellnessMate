from src.agents.data_agent import DataAgent
from src.agents.llm_analytics_agent import LLMAnalyticsAgent
from src.agents.llm_coach_agent import LLMCoachAgent

def run_pipeline():
    # Load data
    data_agent = DataAgent(mode="dataset")
    df = data_agent.get_data("data/raw/fitbit.csv")

    # LLM analytics
    analytics_agent = LLMAnalyticsAgent()
    insights = analytics_agent.run(df)

    # LLM coaching
    coach_agent = LLMCoachAgent()
    plan = coach_agent.generate_plan(insights)

    print("\n=== AI-Generated Insights ===")
    print(insights)

    print("\n=== AI-Generated Wellness Plan ===")
    print(plan)

if __name__ == "__main__":
    run_pipeline()
