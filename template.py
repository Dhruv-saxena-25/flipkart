import os 
from pathlib import Path

project_name = "flipkart"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/data_converter.py",
    f"{project_name}/data_ingestion.py",
    f"{project_name}/retrieval_generation.py",
    "static/style.css",
    "templates/chat.html",
    "setup.py",
    "app.py",
    "requirements.txt",
    ".env"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath, "w") as f:
            pass