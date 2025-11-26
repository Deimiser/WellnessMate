# src/workflow/wellness_graph.py

from src.workflow.state import WellnessState
from src.workflow.nodes import DataNode, AnalyticsNode, CoachNode

class WellnessGraph:
    """
    Simple linear workflow:
    DataNode -> AnalyticsNode -> CoachNode
    """

    def __init__(self):
        self.data_node = DataNode()
        self.analytics_node = AnalyticsNode()
        self.coach_node = CoachNode()

    def run(self, path="data/raw/fitbit.csv"):
        state = WellnessState()

        state = self.data_node.run(state, path)
        state = self.analytics_node.run(state)
        state = self.coach_node.run(state)

        return state
