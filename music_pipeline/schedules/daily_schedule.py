from dagster import ScheduleDefinition
from music_pipeline.jobs.data_pipeline import music_data_pipeline

music_pipeline_schedule = ScheduleDefinition(
    job=music_data_pipeline,
    cron_schedule="0 8 * * *",  # Every day at 8 AM
    name="daily_music_data_schedule"
)
