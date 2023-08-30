import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

root.geometry("1920x1080")
root.configure(background='black')

label = tk.Label(root, text="Bulldog Motorsports ", font=('Arial', 70), bg="black", fg="white")
label.place(x=600, y=50)

imageLogo = Image.open("StatusBoardLogo.png")
logo = ImageTk.PhotoImage(imageLogo)

Logolabel = tk.Label(image=logo, borderwidth=0)
Logolabel.image = logo

Logolabel.place(x= 400, y= 50)


# Controls Collumn


# For percentage bar, overlap an orange rectangle over a white one and adjust the x value

ctrl_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
ctrl_canvas.create_rectangle(0, 0, 300, 400, fill="maroon")

ctrl_canvas.create_text(100, 25, text="Controls", font=("Arial", 20), fill="white")

ctrl_canvas.create_text(165, 67, text="StatusBoard Coding Project", font=("Arial", 8), fill="white", anchor='e')

# percentage bar  ↓↓↓↓
ctrl_canvas.create_rectangle(30, 80, 170, 100, fill="white") # keep static
ctrl_canvas.create_rectangle(30, 80, 120, 100, fill="orange")


ctrl_canvas.place(x=100,y=200)

# PowerTrain Collumn

pwT_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
pwT_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

pwT_canvas.create_text(100, 25, text="PowerTrain", font=("Arial", 20), fill="white")


pwT_canvas.place(x=350,y=200)

# Drivetrain Collumn

drT_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
drT_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

drT_canvas.create_text(100, 25, text="DriveTrain", font=("Arial", 20), fill="white")


drT_canvas.place(x=600,y=200)

# Suspension Collumn

sus_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
sus_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

sus_canvas.create_text(100, 25, text="Suspension", font=("Arial", 20), fill="white")

sus_canvas.place(x=850,y=200)

# Chasis Collumn

chas_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
chas_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

chas_canvas.create_text(100, 25, text="Chasis", font=("Arial", 20), fill="white")


chas_canvas.place(x=1100,y=200)

# Electrical Collumn

elec_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
elec_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

elec_canvas.create_text(100, 25, text="Electrical", font=("Arial", 20), fill="white")


elec_canvas.place(x=1350,y=200)

# Aero Collumn

aero_canvas = tk.Canvas(root, width=200, height=400, borderwidth = 2, relief="raised")
aero_canvas.create_rectangle(0, 0, 300, 500, fill="maroon")

aero_canvas.create_text(100, 25, text="Aero", font=("Arial", 20), fill="white")


aero_canvas.place(x=1600,y=200)


#Bottom Schedule

footerBar = tk.Canvas(root, width= 1000, height = 200, borderwidth = 2, relief="groove" )


footerBar.create_rectangle(0, 0, 1002 , 202, fill="maroon")


footerBar.create_text(150, 40, text="• Interest Meeting 10/7", font=("Helvetica", 20), fill="white", anchor="w")
footerBar.create_text(150, 100, text="• Random Deadline 10/7", font=("Helvetica", 20), fill="white", anchor="w")
footerBar.create_text(150, 160, text="• Fake Meeting 10/7", font=("Helvetica", 20), fill="white", anchor="w")

# first row of important dates   ↑↑↑↑
# Second Row of important dates  ↓↓↓↓

footerBar.create_text(600, 40, text="• Controls Meeting 8/30", font=("Helvetica", 20), fill="white", anchor="w")
footerBar.create_text(600, 100, text="• Michigan Comp 00/00", font=("Helvetica", 20), fill="white", anchor="w")
footerBar.create_text(600, 160, text="• Formula South 00/00", font=("Helvetica", 20), fill="white", anchor="w")

footerBar.place(x= 480, y= 750)

# Important Dates Text

label = tk.Label(root, text="Important Dates", font=('Arial', 55), bg="black", fg="white")
label.place(x=700, y=650)




root.mainloop()
