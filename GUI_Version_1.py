#Import necessry libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame or window
window = Tk()

#Set the geometry of tkinter frame
window.geometry("700x350")
window.title("Fretboard Simulator")

#create integer values for notes
notes = [IntVar() for i in range(6)]

#Create Label for title
program_title = Label(text="Guitar Fretboard Simulator V1.0", font="Helvetica 18 bold").grid(row = 0, column = 2, columnspan = 4, pady = 15)

#Create Labels for chord and note indicators
chord_label = Label(text="Chord: ").grid(row = 7, column = 1, columnspan = 4, pady = 10)
notes_label = Label(text="Notes: ").grid(row = 8, column = 1, columnspan = 4, pady = 10)

#create 6 strings with 12 notes in each
buttons = [[None]*12]*6

for i,string in enumerate(buttons):
    for j, note in enumerate(string):
        buttons[i][j] = Radiobutton(window, variable=notes[i], value=j).grid(row=i+1, column=j, padx=30, pady=4)


#Launch GUI
window.mainloop()
