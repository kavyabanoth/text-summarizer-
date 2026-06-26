import os
import urllib.request as request
import ssl
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size
from pathlib import Path
from textsummarizer.entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Create SSL context that bypasses certificate verification
            ssl_context = ssl._create_unverified_context()
            
            # Use urlopen instead of urlretrieve to support SSL context
            with request.urlopen(self.config.source_URL, context=ssl_context) as response:
                with open(self.config.local_data_file, 'wb') as out_file:
                    out_file.write(response.read())
            
            logger.info(f"{self.config.local_data_file} download completed")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)