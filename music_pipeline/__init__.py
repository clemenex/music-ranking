# music_pipeline/__init__.py

# Expose public interface of the package
from music_pipeline.jobs.data_pipeline import music_data_pipeline
from music_pipeline.schedules.daily_schedule import music_pipeline_schedule  # if you put it in a separate file

__all__ = ["music_data_pipeline", "music_pipeline_schedule"]
