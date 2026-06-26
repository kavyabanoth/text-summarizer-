from pathlib import Path
from textsummarizer.utils.common import read_yaml, create_directories
from textsummarizer.entity import(DataIngestionConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=Path("config/config.yaml")):
        self.config = read_yaml(config_filepath)

        # create artifacts root folder
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return config