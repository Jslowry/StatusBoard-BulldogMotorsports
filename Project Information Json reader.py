
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

"""
How the Function is expected to be used

list_name, list_date, list_percent = ProjectInformationJsonReader("section")
for i in range(len(list_name))
    section_canvas.create_text(x, y, text=list_name[i], font=("Arial", 8), fill="white", anchor='e')
    section_canvas.create_text(x, y, text=list_date[i], font=("Arial", 8), fill="white", anchor='e')

    # percentage bar  ↓↓↓↓
    controls_canvas.create_rectangle(x1, y1, x2, y2, fill="white")  # keep static
    percent = int(list_percent[i]) / 100
    controls_canvas.create_rectangle(x1, y1, x1 + ((x2 - x1) * percent), y2, fill="orange")  # x2 should be = lowest x value plus (max x length times percentage)

"""