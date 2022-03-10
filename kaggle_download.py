import os
import zipfile
project = input('Input the name of the project: ')
os.chdir('C:/Users/admin/Desktop')
if not os.path.isdir('./kaggle_data'):
    os.mkdir('C:/Users/admin/Desktop/kaggle_data')
os.chdir('C:/Users/admin/Desktop/kaggle_data')
os.environ['KAGGLE_USERNAME'] = "korwinbieniek"
os.environ['KAGGLE_KEY'] = "dff0699451f214d2508bbf04fe583fd5"
os.system(f'kaggle competitions download -c {project}')

with zipfile.ZipFile(f'C:/Users/admin/Desktop/kaggle_data/{project}.zip', 'r') as zip_ref:
    zip_ref.extractall('C:/Users/admin/Desktop/kaggle_data')
os.remove(f'{project}.zip')