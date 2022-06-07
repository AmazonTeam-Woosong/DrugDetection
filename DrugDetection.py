import tkinter
import customtkinter
import tkinter as tk
import tkinter.filedialog as fd
import os
from tkinter.ttk import Progressbar
import time
from tkinter import *
import glob
from PIL import ImageTk, Image
from PIL import *
from matplotlib.ft2font import HORIZONTAL

# CREATE WINDOW
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("410x350")     
app.title(" Drug Detection")
app.iconbitmap('icon.ico')

# TOOLBAR
def Help1():
    #Code to be written
    top= Toplevel(app)
    top.geometry("1200x210")
    top.title("Help")
    Label(top, text= "How to use:", font=('Mistral 18 bold')).place(x=50,y=10)
    Label(top,text= "Step 1: Select if the detection will be over an image or a video.", font=('Arial')).place(x=150,y=70)
    Label(top,text= "Step 2: Click the 'Upload' button to choose the file to detect. The file must be in a local storage.", font=('Arial')).place(x=150,y=110)
    Label(top,text= "Step 3: Wait 10 seconds for the detection to process. The results will be displayed automatically in a new window.", font=('Arial')).place(x=150,y=150)
    pass

frame = Frame(app)
frame.pack()
mainmenu = Menu(frame)
mainmenu.add_command(label = "Help", command= Help1)
mainmenu.add_command(label = "Exit", command= app.destroy)
app.config(menu = mainmenu)


# TITLE "DRUG DETECTION"
logo = Image.open("logo.png")
#Resize the Image using resize method
resized_image= logo.resize((400,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
l = Label(app, image = new_image)
l.config(bg="#1A1A1A")
l.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER) 
l.pack()

# SOFTWARE DESCRIPTION TEXT
l2 = Label(app, text = "Our drug detection software is able to detect four types of drugs including heroin, cocaine, shrooms, and marijuana.")
l2.config(fg="grey", bg="#1A1A1A", font =("helvetica", 9), wraplength=650, justify="center")
l2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER) 
l2.pack()

#SEPARATING FRAME
frame3 = Frame(app, width=850, height=30)
frame3.place(x=1, y=1, anchor=tkinter.CENTER)
frame3.config(bg="#1A1A1A")
frame3.pack()

# IMAGE UPLOAD FUNCTION
def upload_file1():
    currdir = os.getcwd()
    tempdir = fd.askopenfilename(parent=app, initialdir=currdir, title='Please select a file')     # the file name
    
    # PROGRESS BAR
    def step():
        for i in range(10):
            app.update_idletasks()
            pb1['value'] += 10
            
            time.sleep(0.1)
    pb1 = Progressbar(app, length=200, mode='determinate')
    pb1.pack(expand=True)
    pb1.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER) 

    cmd_ln = "python detect.py --source " + str(tempdir) + " --weights drugs277.pt --view-img"
    step()
    os.system(cmd_ln)

# VIDEO UPLOAD FUNCTION
def upload_file2():

    currdir = os.getcwd()
    tempdir = fd.askopenfilename(parent=app, initialdir=currdir, title='Please select a file')     # the file name
    
    #progress bar
    def step():
        for i in range(10):
            app.update_idletasks()
            pb1['value'] += 10
            time.sleep(0.1)


    pb1 = Progressbar(app, length=200, mode='determinate')
    pb1.pack(expand=True)
    pb1.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER) 
       
    cmd_ln = "python detect2.py --source " + str(tempdir) + " --weights drugs277.pt --view-img"
    step()
    os.system(cmd_ln)


# UPLOAD BUTTON
button1 = customtkinter.CTkButton(master=app, text="Upload Image", command=upload_file1)
button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


button2 = customtkinter.CTkButton(master=app, text="Upload Video", command=upload_file2)
button2.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

# AMAZON TEAM LOGO
logo2 = Image.open("amazon_logo.png")
#Resize the Image using resize method
resized_image2= logo2.resize((180,180), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
l = Label(app, image = new_image2)
l.config(bg="#1A1A1A")
#l.place(relx=0.5, rely=0.95) 
l.pack(side=tk.BOTTOM, anchor=tkinter.SE)


app.mainloop()