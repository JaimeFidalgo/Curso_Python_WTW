import pandas as pd
import os
import shutil

# Arguments

mapping_file = r"C:\Users\JAIME4560\OneDrive - Willis Towers Watson\Escritorio\Curso_Python_WTW-main (2)\Curso_Python_WTW-main\02_Session_2\excercise\mapping_DV3.xlsx"
input_folder=r"C:\Users\JAIME4560\OneDrive - Willis Towers Watson\Escritorio\Curso_Python_WTW-main (2)\Curso_Python_WTW-main\02_Session_2\excercise"
output_dir = r"C:\Users\JAIME4560\OneDrive - Willis Towers Watson\Escritorio\Curso_Python_WTW-main (2)\Curso_Python_WTW-main\02_Session_2\excercise\outputs"

# Read Excel

df = pd.read_excel(mapping_file)

#print(df)

#Convert df to list

files_list = df.to_numpy().tolist()
#print(files_list)

#Fix list

files_list_fixed = []

for i in files_list:
    files_list_fixed.append(i[0])
    
#print(files_list_fixed)

# Extract paths of files

matching_files = []
for root, directories, filenames in os.walk(input_folder):
    for filename in filenames:
        if(filename in files_list_fixed):
            matching_files.append(os.path.join(root,filename))

for file in matching_files:
    shutil.copy(file, output_dir)
    

    



    

