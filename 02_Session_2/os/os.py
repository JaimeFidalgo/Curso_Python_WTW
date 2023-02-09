import os

# Paths

file = "Assumptions.xlsx"

WD = r"C:\Users\JAIME4560\OneDrive - Willis Towers Watson\Escritorio\Curso_Python_WTW-main (2)\Curso_Python_WTW-main\02_Session_2\os\test"

# Path concatenation

file_path = os.path.join(WD,file)

print(file_path)

# listdir()

dir = os.listdir(WD)

print(dir)

#Create Folder

folder_name = "folder"

folder_path = os.path.join(WD,folder_name)

os.makedirs(folder_path)

# Listar elementos en un directorio

dirs