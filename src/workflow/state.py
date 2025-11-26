# src/workflow/state.py

class WellnessState:
    """
    Central pipeline state shared across all nodes.
    """

    def __init__(self):
        self.data = None
        self.insights = None
        self.plan = None

    def __repr__(self):
        return f"WellnessState(data={type(self.data)}, insights={self.insights}, plan={self.plan})"
