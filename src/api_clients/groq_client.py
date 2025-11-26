import os
import requests

class GroqClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")

    def chat(self, model, messages, temperature=0.2, max_tokens=500):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        response = requests.post(self.base_url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Groq API Error: {response.text}")

        return response.json()["choices"][0]["message"]["content"]
