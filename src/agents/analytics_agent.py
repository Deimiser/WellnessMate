class AnalyticsAgent:
    def detect_trends(self, df):
        avg_steps = df['steps'].mean()

        insights = {
            "avg_steps": avg_steps,
            "steps_increasing": df['steps'].iloc[-1] > df['steps'].iloc[0]
        }
        return insights
