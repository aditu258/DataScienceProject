from dataclasses import dataclass
from pathlib import Path

@dataclass ##decorator
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict
    
@dataclass()
class DataTransformationConfig:
    root_dir: Path
    data_path: Path