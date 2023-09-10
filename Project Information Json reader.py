
projects = {"controls": [{"projectname": "pedal tray", "date": "091223", "percent": "76"}, {"projectname": "steering", "date": "084723", "percent": "45"}, {"projectname": "pedal tray", "date": "091223", "percent": "76"}, {"projectname": "pedal tray", "date": "091223", "percent": "76"}, {"projectname": "pedal tray", "date": "091223", "percent": "76"}, {"projectname": "pedal tray", "date": "091223", "percent": "76"}, {"projectname": "pedal tray", "date": "091223", "percent": "76"}],
            "drivetrain": [{"projectname": "sprocket", "date": "091223", "percent": "76"}, {"projectname": "chain", "date": "084723", "percent": "45"}],
            "aero": [{"projectname": "Top Wing", "date": "091223", "percent": "76"}, {"projectname": "Bottom Wing", "date": "084723", "percent": "45"}],
            "chassis": [{"projectname": "Chassis", "date": "091223", "percent": "76"}],
            "electrical": [{"projectname": "Wires", "date": "091223", "percent": "0"}],
            "power train": [{"projectname": "Wires", "date": "091223", "percent": "0"}],
            "suspension": [{"projectname": "Wires", "date": "091223", "percent": "0"}]
}


# section is a string variable for which section's information needs to be pulled
def ProjectInformationJsonReader(section):
    project_name_list = []
    date_list = []
    percent_list = []
    max_items = 5
    for i in range(len(projects[f"{section}"])):
        if i == max_items:
            break
        project_name_list.append(projects[f"{section}"][i]["projectname"])
        date_list.append(projects[f"{section}"][i]["date"])
        percent_list.append(projects[f"{section}"][i]["percent"])
    return project_name_list, date_list, percent_list


list_name, list_date, list_percent = ProjectInformationJsonReader("controls")
print(list_name)
print(list_date)
print(list_percent)
