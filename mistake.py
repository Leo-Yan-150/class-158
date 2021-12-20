from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()
root.title("M I S T A K E")
root.geometry("600x400")

try:
    root.geometry("yes")
except:
    print("boueh you cannot have a string in a .geometry setting, change that right now or else...")
    
n1 = 1
n2 = "2"
try:
    print(n1+n2)
except(TypeError):
    print("boueh you cannot add a str variable with a int veriable, you cant even add str variables unless you want to concat them")

try:
    print(n1+whateverthisvariableisidcaboutitsincetherearenosuchvariablethatexists)
except NameError:
    print("why did you type out all of that my dude, just to get errors?")

iinput = Entry(root)

def something():
    thiny=iinput.get()
    try:
        print(thiny+5)
    except(TypeError):
        print("I gave you a error box, now please let my family go.")
        messagebox.showinfo("E R R O R", "this is a error message...but better that the console...I guess.")

boton = Button(root, text="click this for a mistake", command = something)
iinput.pack()
boton.pack()

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school