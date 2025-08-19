# import necessary libraries
from tkinter import *
from datetime import date

# Create window
root = Tk()
root.title('Getting Started With Widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="Hey There!", fg="white", bg = "#072F5F", height = 1, width = 300)

# Add Label for getting name as input from user
# use entry widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Function to display a message
def display():
     
     # read input given by user
     name = name_entry.get()

     # Declaring a global variable
     # to make it accesible anywhere in the program
     global message
     message = "Wellcome to the Application!\nToday's Date is:"
     greet = "Hello "+name+"\n"

     # Dispaly details in a text box
     # Specify where to add the details inside the text box
     text_box.insert(END, greet)
     text_box.insert(END, message)
     text_box.insert(END, date.today())

# Add a text widget to display info
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, Display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg = 'white')

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()