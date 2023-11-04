import os
import shutil

def updateExcelFile():
    try:
        filepath = "C:/Users/FSAE/Downloads/StatusBoardTest/StatusBoardBulldogMotorsports-main/Master Schedule 2024.xlsx"
        os.remove(filepath)# removes old first
    except:
        print("No File")
    # current_directory = os.getcwd()
    destination_path = os.path.join("C:/Users/FSAE/Downloads/StatusBoardTest/StatusBoardBulldogMotorsports-main", os.path.basename("C:/Users/FSAE/Downloads/StatusBoardTest/StatusBoardBulldogMotorsports-main/Master Schedule 2024.xlsx")) # 
    source_file = "C:/Users/FSAE/OneDrive - Mississippi State University/Documents - MSSTATE Formula SAE (UserCreated)/Mississippi State FSAE/FSAE 2024/Management/Master Schedule 2024.xlsx"
    shutil.copy(source_file, destination_path) # The two lines above are unique to each computer D:
    