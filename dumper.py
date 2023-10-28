from main import pullDataFromExcel
import json


def dumpProjectData2JSON():
    projectData = pullDataFromExcel()
    with open('excelData.json', 'w') as json_file:
        json.dump(projectData, json_file)
