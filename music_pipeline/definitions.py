from dagster import Definitions, ScheduleDefinition, load_assets_from_modules
from music_pipeline import assets
from music_pipeline.jobs.data_pipeline import music_data_pipeline

all_assets = load_assets_from_modules([assets])

music_pipeline_schedule = ScheduleDefinition(
    job=music_data_pipeline,
    cron_schedule="0 8 * * *",
    name="daily_music_data_schedule"
)

defs = Definitions(
    assets=all_assets,
    jobs=[music_data_pipeline],
    schedules=[music_pipeline_schedule]
)
