import pandas as pd
from src.api_clients.groq_client import GroqClient

class AnalyticsAgent:
    def __init__(self, model="llama-3.1-70b-versatile"):
        self.llm = GroqClient()
        self.model = model

    def detect_trends(self, df: pd.DataFrame):
        # Summaries for the LLM
        summary = {
            "avg_steps": float(df["steps"].mean()),
            "min_steps": float(df["steps"].min()),
            "max_steps": float(df["steps"].max()),
            "avg_sleep": float(df["sleep_hours"].mean()),
        }

        prompt = f"""
        You are a health analytics expert.
        Based on the following stats:

        {summary}

        Provide:
        - Key trends
        - Any warnings
        - What the user's body is doing
        - 3 improvement ideas

        Return JSON only.
        """

        result = self.llm.call_llm(self.model, prompt)
        return result
