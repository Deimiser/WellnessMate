from src.api_clients.groq_client import GroqClient

class LLMAnalyticsAgent:
    def __init__(self, model="llama-3.1-70b-versatile"):
        self.client = GroqClient()
        self.model = model

    def run(self, df):
        text_stats = df.describe(include="all").to_string()

        prompt = f"""
You are a wellness analytics expert.

Given the dataset statistics:

{text_stats}

Generate insights about user's fitness, sleep, and lifestyle patterns.
Highlight positive trends + risks + anomalies.
Return the output in bullet points.
"""

        messages = [
            {"role": "system", "content": "You analyze health data."},
            {"role": "user", "content": prompt}
        ]

        return self.client.chat(model=self.model, messages=messages)
