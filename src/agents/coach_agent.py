class CoachAgent:
    def create_daily_plan(self, summary, insights, goal="general"):
        plans = []

        for _, row in summary.iterrows():
            plans.append({
                "date": row['date'].strftime("%Y-%m-%d"),
                "tasks": [
                    "Walk 5,000–8,000 steps",
                    "Drink 2L water",
                    "Sleep 7–8 hours",
                ]
            })
        return plans
