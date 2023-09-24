import tkinter as tk
from PIL import Image, ImageTk
import json 
import openpyxl 
import time
from datetime import date

start_time = time.time()


# start_time = time.time()

root = tk.Tk()

root.geometry("1920x1080")
root.configure(background='black')
root.attributes('-fullscreen', True)

label = tk.Label(root, text="Bulldog Motorsports ", font=('Arial', 70), bg="black", fg="white")
label.place(x=600, y=50)

MSU_Maroon = "#5D1725"

# Images stored ↓↓↓↓

imageLogo = Image.open("StatusBoardLogo.png")
logo = ImageTk.PhotoImage(imageLogo)

imageGear = Image.open("gearIcon.png")
gear = ImageTk.PhotoImage(imageGear, width=20, height=20)

imageExit = Image.open("redX.png")
redX = ImageTk.PhotoImage(imageExit)

imageSave = Image.open("saveButton.png")
saveButton = ImageTk.PhotoImage(imageSave)

imageExitMaroon = Image.open("maroonX.png")
maroonX = ImageTk.PhotoImage(imageExitMaroon)

imageSaveExit = Image.open("save and exit.png")
saveExit = ImageTk.PhotoImage(imageSaveExit)

# Placing Logo
Logo_label = tk.Label(image=logo, borderwidth=0)
Logo_label.image = logo

Logo_label.place(x=400, y=50)


# Populate Column

# Controls Column

# For percentage bar, overlap an orange rectangle over a white one and adjust the x value

controls_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
controls_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


controls_canvas.create_text(100, 25, text="Controls", font=("Arial", 25), fill="white")

# controls_canvas.create_text(165, 67, text="StatusBoard Coding Project", font=("Arial", 8), fill="white", anchor='e')

# percentage bar  ↓↓↓↓

# controls_canvas.create_rectangle(30, 80, 170, 100, fill="white")
# controls_canvas.create_rectangle(30, 80, 120, 100, fill="orange")

controls_canvas.place(x=100, y=200)


# PowerTrain Column

powerTrain_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
powerTrain_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


powerTrain_canvas.create_text(100, 25, text="PowerTrain", font=("Arial", 25), fill="white")

powerTrain_canvas.place(x=350, y=200)


# Drivetrain Column

driveTrain_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
driveTrain_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


driveTrain_canvas.create_text(100, 25, text="DriveTrain", font=("Arial", 25), fill="white")

driveTrain_canvas.place(x=600, y=200)


# Suspension Column

suspension_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
suspension_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


suspension_canvas.create_text(100, 25, text="Suspension", font=("Arial", 25), fill="white")

suspension_canvas.place(x=850, y=200)


# Chassis Column

chassis_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
chassis_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


chassis_canvas.create_text(100, 25, text="Chassis", font=("Arial", 25), fill="white")

chassis_canvas.place(x=1100, y=200)

# Electrical Column


electrical_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
electrical_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


electrical_canvas.create_text(100, 25, text="Electrical", font=("Arial", 25), fill="white")

electrical_canvas.place(x=1350, y=200)


# Aero Column


aero_canvas = tk.Canvas(root, width=200, height=550, borderwidth=2, relief="raised")
aero_canvas.create_rectangle(0, 0, 300, 600, fill=MSU_Maroon)


aero_canvas.create_text(100, 25, text="Aero", font=("Arial", 25), fill="white")

aero_canvas.place(x=1600, y=200)


# Bottom Schedule


footerBar = tk.Canvas(root, width=1500, height=150, borderwidth=2, relief="groove")
footerBar.create_rectangle(0, 0, 1502, 152, fill=MSU_Maroon)


footerBar.place(x=250, y=850)


# Important Dates Text
label = tk.Label(root, text="Important Dates", font=('Arial', 55), bg="black", fg="white")
label.place(x=715, y=760)


def findLastProjectRow():
    excelOpen = openpyxl.load_workbook('Master Schedule 2024.xlsx')
    activeExcel = excelOpen.active
    for i in range(8, 500):
        cell_section = activeExcel.cell(row=i, column=1)
        if cell_section.value is None:
            break
    return i


# there is a crash if there is a space after a section name
# there are several possible ways to fix this, but I don't know how this function works to fix it.
# also it seems to only get the system name for the project name, wouldn't it make more sense to get more information?
# it probably should get some combination of the system name, phase, part, and the person assigned to it.
# ex. System name, part, phase = Steering, Wheel, Design  or  Floor plate, Mold, Manufacture
# These examples while longer give a good idea of what is being done
# rather than the steering or floor plate that would display currently

def pullDataFromExcel():
    # write a with open json.dump() data function in here, so we can get some fresh data on boot up
    excelOpen = openpyxl.load_workbook('Master Schedule 2024.xlsx')
    activeExcel = excelOpen.active
    max_row = findLastProjectRow()  # Where Function?

    projects = {"Controls": [], "Drivetrain":  [], "Powertrain": [], "Suspension": [], "Chassis": [], "Electrical": [], "Aerodynamics": []}
    for i in range(8, max_row):
        cell_section = activeExcel.cell(row=i, column=1)
        cell_percentage = activeExcel.cell(row=i, column=6)
        # cell_date = activeExcel.cell(row=i, column=7)
        cell_system = activeExcel.cell(row=i, column=2)
        """
        today = date.today()  # datetime.date Datatype
        # print(type(activeExcel.cell(row=i, column=7)))  # <class 'openpyxl.cell.cell.Cell'>
        print(activeExcel.cell(row=i, column=7).get_time_format)
        print(type(activeExcel.cell(row=i, column=7).get_time_format))
        """
        section_value = cell_section.value
        cell_section = section_value.strip()

        # removed cell_percentage.value != 0 because it causes the json to be super empty
        # it would make more sense to check the start date to see if the project should be
        # started which is column G in Excel
        # which could use the unused cell_date for a more accurate list of what needs to be started
        if cell_percentage.value != 1.0 and cell_section != "Business":
            projects[cell_section].append({"projectname": cell_system.value, "percent": cell_percentage.value})

    excelOpen.close()  # This was behind the return function this should be here if you want it to run.
    return projects


def dumpProjectData2JSON():
    projectData = pullDataFromExcel()
    with open('excelData.json', 'w') as json_file:
        json.dump(projectData, json_file)


def getProjectData():
    with open('excelData.json', 'r') as json_file:
        projectData = json.load(json_file)
    return projectData


def displayControlsData():
    projectData = getProjectData()
    
    g = 0

    for i in range(7):
        controls_canvas.create_text(30, 75 + g, text=projectData["Controls"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        controls_canvas.create_text(30, 98 + g, text=f'{int(projectData["Controls"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Controls"][i]["percent"]
        controls_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            controls_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            controls_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displayPowerTrainData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        powerTrain_canvas.create_text(30, 75 + g, text=projectData["Powertrain"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        powerTrain_canvas.create_text(30, 98 + g, text=f'{int(projectData["Powertrain"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Powertrain"][i]["percent"]
        powerTrain_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            powerTrain_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            powerTrain_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displayDriveTrainData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        driveTrain_canvas.create_text(30, 75 + g, text=projectData["Drivetrain"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        driveTrain_canvas.create_text(30, 98 + g, text=f'{int(projectData["Drivetrain"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Drivetrain"][i]["percent"]
        driveTrain_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            driveTrain_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            driveTrain_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displaySuspensionData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        suspension_canvas.create_text(30, 75 + g, text=projectData["Suspension"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        suspension_canvas.create_text(30, 98 + g, text=f'{int(projectData["Suspension"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Suspension"][i]["percent"]
        suspension_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            suspension_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            suspension_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displayChassisData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        chassis_canvas.create_text(30, 75 + g, text=projectData["Chassis"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        chassis_canvas.create_text(30, 98 + g, text=f'{int(projectData["Chassis"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Chassis"][i]["percent"]
        chassis_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            chassis_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            chassis_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displayElectricalData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        electrical_canvas.create_text(30, 75 + g, text=projectData["Electrical"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        electrical_canvas.create_text(30, 98 + g, text=f'{int(projectData["Electrical"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Electrical"][i]["percent"]
        electrical_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            electrical_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            electrical_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70


def displayAeroData():
    projectData = getProjectData()

    g = 0

    for i in range(7):
        aero_canvas.create_text(30, 75 + g, text=projectData["Aerodynamics"][i]["projectname"], font=("Arial", 8), fill="white", anchor='w')
        aero_canvas.create_text(30, 98 + g, text=f'{int(projectData["Aerodynamics"][i]["percent"] * 100)}%', font=("Arial", 8), fill="white", anchor='e')
        percentage = projectData["Aerodynamics"][i]["percent"]
        aero_canvas.create_rectangle(30, 88 + g, 170, 108 + g, fill="white")
        if percentage == 0.00:
            aero_canvas.create_rectangle(30, 88 + g, 30, 108 + g, fill="orange")
        else:
            aero_canvas.create_rectangle(30, 88 + g, 30 + (140 * percentage), 108 + g, fill="orange")
        g += 70

# Button that calls edit function for important Dates (CONTAINS MANY FUNCTIONS TO
# READ AND WRITE TO JSON AND TO DISPLAY DATES)


def editButton():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Important Dates")
    edit_window.geometry("560x350+70+70")
    edit_window.overrideredirect(True)
    edit_window.configure(background=MSU_Maroon, borderwidth=7, relief="solid", highlightthickness=3)

    # Text Entry Boxes Defined and placed below

    task1 = tk.Label(edit_window, text="Edit task one:")
    task1Entry = tk.Entry(edit_window)
    task1EntryDate = tk.Entry(edit_window)
    
    task2 = tk.Label(edit_window, text="Edit task two:")
    task2Entry = tk.Entry(edit_window)
    task2EntryDate = tk.Entry(edit_window)
    
    task3 = tk.Label(edit_window, text="Edit task three:")
    task3Entry = tk.Entry(edit_window)
    task3EntryDate = tk.Entry(edit_window)
    
    task4 = tk.Label(edit_window, text="Edit task four:")
    task4Entry = tk.Entry(edit_window)
    task4EntryDate = tk.Entry(edit_window)
    
    task5 = tk.Label(edit_window, text="Edit task five:")
    task5Entry = tk.Entry(edit_window)
    task5EntryDate = tk.Entry(edit_window)

    task6 = tk.Label(edit_window, text="Edit task 6:")
    task6Entry = tk.Entry(edit_window)
    task6EntryDate = tk.Entry(edit_window)

    # Sets the data from the entries to a dictionary

    def setImportantDates():
        data = {
            "task1": {
                "task": task1Entry.get(),
                "date": task1EntryDate.get()
            },
            "task2": {
                "task": task2Entry.get(),
                "date": task2EntryDate.get()
            },
            "task3": {
                "task": task3Entry.get(),
                "date": task3EntryDate.get()
            },
            "task4": {
                "task": task4Entry.get(),
                "date": task4EntryDate.get()
            },
            "task5": {
                "task": task5Entry.get(),
                "date": task5EntryDate.get()
            },
            "task6": {
                "task": task6Entry.get(),
                "date": task6EntryDate.get()
            }
        }
        # writes it to important_dates.json
        with open("important_dates.json", "w") as json_file:
            json.dump(data, json_file)

    # reads the data that was put into important_dates and returns the data in the form of a dictionary

    # places the data from the dictionary into displayable text

    # will update the data on closure of the edit window
    def exit_editButton():
        setImportantDates()
        displayImportantDates()
        edit_window.destroy()

    # save_button = tk.Button(edit_window, text="Save", image=saveButton, borderwidth=0, highlightthickness=0, command=setImportantDates)
    exit_button = tk.Button(edit_window, text="Exit", command=exit_editButton, image=saveExit, borderwidth=0, highlightthickness=0)

    # Placing text boxes for important dates entry
    task1.place(x=60, y=10)
    task1Entry.place(x=50, y=35)
    task1EntryDate.place(x=50, y=60)
    
    task2.place(x=60, y=85)
    task2Entry.place(x=50, y=110)
    task2EntryDate.place(x=50, y=135)

    task3.place(x=60, y=160)
    task3Entry.place(x=50, y=185)
    task3EntryDate.place(x=50, y=210)

    task4.place(x=380, y=10)
    task4Entry.place(x=370, y=35)
    task4EntryDate.place(x=370, y=60)

    task5.place(x=380, y=85)
    task5Entry.place(x=370, y=110)
    task5EntryDate.place(x=370, y=135)

    task6.place(x=380, y=160)
    task6Entry.place(x=370, y=185)
    task6EntryDate.place(x=370, y=210)

    exit_button.place(x=160, y=270)


# Button to access edit function
ImpDatesButton = tk.Button(text="Edit Important Dates", command=editButton, image=gear, borderwidth=0, highlightthickness=0)

ImpDatesButton.place(x=85, y=20)

# Display without pressing edit   HAS ISSUES BECAUSE IT OVERLAPS EDITED DATA


def getImportantDates():
    with open("important_dates.json", "r") as json_file:
        importantDataList = json.load(json_file)
    return importantDataList


def displayImportantDates():

    data = getImportantDates()

    footerBar.create_rectangle(0, 0, 1502, 152, fill=MSU_Maroon)  # Drawing over the old maroon rectangle
    
    footerBar.create_text(150, 40, text=data["task1"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
    footerBar.create_text(150, 110, text=data["task2"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
    
    footerBar.create_text(650, 40, text=data["task3"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
    footerBar.create_text(650, 110, text=data["task4"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
    
    footerBar.create_text(1100, 40, text=data["task5"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
    footerBar.create_text(1100, 110, text=data["task6"]["task"], font=("Helvetica", 20), fill="white", anchor="w")


displayImportantDates()

dumpProjectData2JSON()

displayControlsData()
displayPowerTrainData()
displayDriveTrainData()
displaySuspensionData()
displayChassisData()
displayElectricalData()
displayAeroData()

# Exit button for entire program

ExitButton = tk.Button(text="Exit", command=root.destroy, image=redX, borderwidth=0, highlightthickness=0)

ExitButton.place(x=1830, y=30)

print("--- %s seconds ---" % (time.time() - start_time))


root.mainloop()
