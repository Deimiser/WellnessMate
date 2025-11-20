class PlannerAgent:
    def create_task_plan(self):
        return {
            "tasks": [
                {"agent": "DataAgent", "action": "load_data"},
                {"agent": "AnalyticsAgent", "action": "analyze"},
                {"agent": "CoachAgent", "action": "create_plan"}
            ]
        }
