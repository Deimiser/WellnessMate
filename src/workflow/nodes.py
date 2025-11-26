# src/workflow/nodes.py

from src.agents.data_agent import DataAgent
from src.agents.analytics_agent import AnalyticsAgent
from src.agents.coach_agent import CoachAgent

class DataNode:
    def __init__(self, mode="dataset"):
        self.agent = DataAgent(mode=mode)

    def run(self, state, path="data/raw/fitbit.csv"):
        state.data = self.agent.get_data(path)
        return state


class AnalyticsNode:
    def __init__(self):
        self.agent = AnalyticsAgent()

    def run(self, state):
        if state.data is None:
            raise ValueError("AnalyticsNode: No data in state")

        state.insights = self.agent.detect_trends(state.data)
        return state


class CoachNode:
    def __init__(self):
        self.agent = CoachAgent()

    def run(self, state):
        if state.data is None or state.insights is None:
            raise ValueError("CoachNode: Missing data or insights in state")

        state.plan = self.agent.create_daily_plan(state.data, state.insights)
        return state
