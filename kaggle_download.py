import os
import zipfile
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
data_dir = Path("./data")
os.system('kaggle c list')
project = input('Input the name of the project: ')
project_dir = data_dir/project
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)
if not os.path.isdir(project_dir):
    os.mkdir(project_dir)

os.system(f'kaggle competitions download -c {project}')
zip_file_path = f"./{project}.zip"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(project_dir)
os.remove(f'{project}.zip')