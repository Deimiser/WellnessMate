import pandas as pd

class DataAgent:
    def __init__(self, mode="dataset"):
        self.mode = mode  # "dataset" or "live"

    def get_data(self, source):
        if self.mode == "dataset":
            return self.load_dataset(source)
        elif self.mode == "live":
            return self.load_live_api(source)
        else:
            raise ValueError("Invalid mode")

    def load_dataset(self, file_path):
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])

        daily_summary = df.groupby('date').agg({
            'steps': 'sum',
            'calories': 'sum',
            'sleep_hours': 'mean',
            'resting_hr': 'mean'
        }).reset_index()

        return daily_summary

    def load_live_api(self, api_client):
        raw_data = api_client.fetch_latest()  
        return self.aggregate(raw_data)

    def aggregate(self, df):
        return df.groupby('date').agg({
            'steps': 'sum',
            'calories': 'sum',
            'sleep_hours': 'mean',
            'resting_hr': 'mean'
        }).reset_index()
