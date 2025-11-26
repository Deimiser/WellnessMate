from src.api_clients.groq_client import GroqClient

class CoachAgent:
    def __init__(self, model="llama-3.1-70b-versatile"):
        self.llm = GroqClient()
        self.model = model

    def create_daily_plan(self, df, insights):
        prompt = f"""
        You are a certified wellness & fitness coach.

        Use the following insights to generate a DAILY PLAN:

        Insights: {insights}

        Produce:
        - Morning routine
        - Afternoon routine
        - Evening routine
        - Hydration plan
        - Mobility + stretching plan
        - Dietary notes

        Output JSON only.
        """

        result = self.llm.call_llm(self.model, prompt)
        return result
