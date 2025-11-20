# WellnessMate
Multi-agent wellness assistant that analyzes time-series health data, generates insights, and creates personalized daily/weekly wellness plans using LLM-powered agents.


WellnessMate is a modular Python project that leverages multi-agent architecture and large language models to help users monitor, analyze, and improve their wellness. The system includes:
DataAgent: Ingests and cleans raw fitness data from CSV files or live APIs (Fitbit, Google Fit, Apple Health).
AnalyticsAgent: Detects trends, correlations, and anomalies in wellness metrics.
CoachAgent: Generates personalized daily and weekly wellness plans with actionable tasks and reminders.
PlannerAgent: Orchestrates the pipeline, decides which agents to call, and produces structured task plans.
The project supports local datasets or live API integration, outputs JSON-based insights and wellness plans, and is designed for safe, privacy-conscious usage.
