from pathlib import Path
import os
import logging

list_of_files = [
    "./github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/utils/__init__.py",
    "src/utils/training_pipeline.py",
    "src/utils/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py"
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    # Create directories if they do not exist
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file {filename}") 
    
    # Create the file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Just create an empty file