from src.api_clients.groq_client import GroqClient

class PlannerAgent:
    def __init__(self, model="llama-3.1-70b-versatile"):
        self.llm = GroqClient()
        self.model = model

    def decide_tasks(self, user_goal="daily wellness improvement"):
        prompt = f"""
        You are a systems orchestrator.

        User Goal: "{user_goal}"

        Decide which agents to call and in what order.
        Valid agents:
        - DataAgent
        - AnalyticsAgent
        - CoachAgent

        Return JSON example:
        {{"pipeline": ["DataAgent", "AnalyticsAgent", "CoachAgent"]}}
        """

        result = self.llm.call_llm(self.model, prompt)
        return result
