import tkinter as tk
from PIL import Image, ImageTk
import json


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
gear = ImageTk.PhotoImage(imageGear, width = 20, height = 20)

imageExit = Image.open("redX.png")
redX = ImageTk.PhotoImage(imageExit)

imageSave = Image.open("saveButton.png")
saveButton = ImageTk.PhotoImage(imageSave)

imageExitMaroon = Image.open("maroonX.png")
maroonX = ImageTk.PhotoImage(imageExitMaroon)

#Placing Logo

Logolabel = tk.Label(image=logo, borderwidth=0)
Logolabel.image = logo

Logolabel.place(x= 400, y= 50)





# Controls Collumn


# For percentage bar, overlap an orange rectangle over a white one and adjust the x value

ctrl_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
ctrl_canvas.create_rectangle(0, 0, 300, 400, fill=MSU_Maroon)

ctrl_canvas.create_text(100, 25, text="Controls", font=("Arial", 20), fill="white")

ctrl_canvas.create_text(165, 67, text="StatusBoard Coding Project", font=("Arial", 8), fill="white", anchor='e')

# percentage bar  ↓↓↓↓
ctrl_canvas.create_rectangle(30, 80, 170, 100, fill="white") # keep static
ctrl_canvas.create_rectangle(30, 80, 120, 100, fill="orange")


ctrl_canvas.place(x=100,y=200)

# PowerTrain Collumn

pwT_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
pwT_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

pwT_canvas.create_text(100, 25, text="PowerTrain", font=("Arial", 20), fill="white")


pwT_canvas.place(x=350,y=200)

# Drivetrain Collumn

drT_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
drT_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

drT_canvas.create_text(100, 25, text="DriveTrain", font=("Arial", 20), fill="white")


drT_canvas.place(x=600,y=200)

# Suspension Collumn

sus_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
sus_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

sus_canvas.create_text(100, 25, text="Suspension", font=("Arial", 20), fill="white")

sus_canvas.place(x=850,y=200)

# Chasis Collumn

chas_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
chas_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

chas_canvas.create_text(100, 25, text="Chasis", font=("Arial", 20), fill="white")


chas_canvas.place(x=1100,y=200)

# Electrical Collumn

elec_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
elec_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

elec_canvas.create_text(100, 25, text="Electrical", font=("Arial", 20), fill="white")


elec_canvas.place(x=1350,y=200)

# Aero Collumn

aero_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
aero_canvas.create_rectangle(0, 0, 300, 500, fill=MSU_Maroon)

aero_canvas.create_text(100, 25, text="Aero", font=("Arial", 20), fill="white")


aero_canvas.place(x=1600,y=200)


#Bottom Schedule

footerBar = tk.Canvas(root, width= 1000, height = 200, borderwidth = 2, relief="groove" )
footerBar.create_rectangle(0, 0, 1002 , 202, fill=MSU_Maroon)

footerBar.place(x= 480, y= 750)


# Important Dates Text

label = tk.Label(root, text="Important Dates", font=('Arial', 55), bg="black", fg="white")
label.place(x=700, y=650)







#Button that calls edit function for important Dates (CONTAINS MANY FUNCTIONS TO READ AND WRITE TO JSON AND TO DISPLAY DATES)


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
            json_file.close

    #reads the data that was put into important_dates and returns the data in the form of a dictionary
    
    def getImportantDates():
        with open("important_dates.json", "r") as json_file:
            importantDataList = json.load(json_file)
            json_file.close
        return importantDataList


    # places the data from the dictionary into displayable text
    
    def displayImportantDates():
        footerBar.delete("text") # deletes any previous values displayed in the footer

        data = getImportantDates()
        for i in range(3):
            footerBar.create_text(150, 40, text=data["task1"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
            footerBar.create_text(150, 100, text=data["task2"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
            footerBar.create_text(150, 160, text=data["task3"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
            for i in range(3):
                footerBar.create_text(600, 40, text=data["task4"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
                footerBar.create_text(600, 100, text=data["task5"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
                footerBar.create_text(600, 160, text=data["task6"]["task"], font=("Helvetica", 20), fill="white", anchor="w")

    # will update the data on closure of the edit window
    
    
    def exit_editButton():
        displayImportantDates()
        edit_window.destroy()

    
    save_button = tk.Button(edit_window, text="Save",image=saveButton, borderwidth=0, highlightthickness=0, command=setImportantDates)
    exit_button = tk.Button(edit_window, text="Exit", command=exit_editButton, image = maroonX, borderwidth=0, highlightthickness=0)
    
    #Placing textboxes for important dates entry
    task1.place(x= 60, y= 10)
    task1Entry.place(x= 50, y= 35)
    task1EntryDate.place(x= 50, y=60)
    
    task2.place(x= 60, y= 85)
    task2Entry.place(x= 50, y= 110)
    task2EntryDate.place(x= 50, y= 135)

    task3.place(x= 60, y= 160)
    task3Entry.place(x= 50, y= 185)
    task3EntryDate.place(x= 50, y= 210)

    task4.place(x= 380, y= 10)
    task4Entry.place(x= 370, y= 35)
    task4EntryDate.place(x= 370, y= 60)

    task5.place(x= 380, y= 85)
    task5Entry.place(x= 370, y= 110)
    task5EntryDate.place(x= 370, y= 135)

    task6.place(x= 380, y= 160)
    task6Entry.place(x= 370, y= 185)
    task6EntryDate.place(x= 370, y= 210)

    save_button.place(x= 110, y= 270)
    exit_button.place(x= 505, y= 3)







# Button to access edit function 


ImpDatesButton = tk.Button(text="Edit Important Dates", command = editButton, image=gear, borderwidth=0, highlightthickness=0)

ImpDatesButton.place(x = 85, y = 30)

# Display without pressing edit   HAS ISSUES BECUASE IT OVERLAPS EDITTED DATA

def getImportantDates():
        with open("important_dates.json", "r") as json_file:
            importantDataList = json.load(json_file)
            json_file.close
        return importantDataList


def displayImportantDates():
    footerBar.delete("text") # deletes any previous values displayed in the footer

    data = getImportantDates()
    for i in range(3):
        footerBar.create_text(150, 40, text=data["task1"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
        footerBar.create_text(150, 100, text=data["task2"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
        footerBar.create_text(150, 160, text=data["task3"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
        for i in range(3):
            footerBar.create_text(600, 40, text=data["task4"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
            footerBar.create_text(600, 100, text=data["task5"]["task"], font=("Helvetica", 20), fill="white", anchor="w")
            footerBar.create_text(600, 160, text=data["task6"]["task"], font=("Helvetica", 20), fill="white", anchor="w")


displayImportantDates()

# Exit button for entire program

ExitButton = tk.Button(text="Exit", command=root.destroy, image = redX, borderwidth=0, highlightthickness=0)

ExitButton.place(x=1830, y= 30)



root.mainloop()
