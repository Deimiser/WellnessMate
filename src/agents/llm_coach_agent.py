from src.api_clients.groq_client import GroqClient

class LLMCoachAgent:
    def __init__(self, model="llama-3.1-70b-versatile"):
        self.client = GroqClient()
        self.model = model

    def generate_plan(self, insights):
        prompt = f"""
You are a senior health coach.

Based on these insights:

{insights}

Create a personalized daily wellness plan with:
- Steps goal  
- Sleep goal  
- Hydration goal  
- Stress-reduction practices  
- Nutrition recommendation  
- Motivation message  

Return the plan in JSON with clear keys.
"""

        messages = [
            {"role": "system", "content": "You generate personalized wellness plans."},
            {"role": "user", "content": prompt},
        ]

        return self.client.chat(model=self.model, messages=messages)
