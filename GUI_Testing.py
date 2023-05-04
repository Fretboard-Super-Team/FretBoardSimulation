from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# given i for the string index and j for the note index return a list of notes from the 2d array
def getCurrentNote(allNotes, currentSelectedNoteIndex):
    return [allNotes[i][j] for i, j in currentSelectedNoteIndex]

def main():

    window = Tk()
    window.title("Fretboard Simulator V2")
    window.geometry("1220x350")

    # Creating Fretboard Label Widget (fretBoardTitle)
    fretBoardTitle = Label(window, text='FretBoard Simulation Version 2.0', font=("Times", "18", "bold underline"))
    fretBoardTitle.grid(row=0, column=2, columnspan=4, pady=15)

    # Creating the Guitar Neck Frame (guitarFrame)
    guitarFrame = Frame(window, width=1120, height=225)
    guitarFrame.grid(row=1, column=0, columnspan=4, pady=15)
    guitarFrame.configure(background='#0ee0c7', relief="solid")
    
    # Create 6 strings with 12 notes in each (allNotes)
    # Create integer values for notes (selectedNotes)
    # Create an Array to Store previous buttons pressed (pastSelectedNotes)
    allNotes = [[Note] * 12] * 6
    selectedNotes = []
    pastSelectedNotes = [0] * 6

        

    # BackRound Image
    image = Image.open("colored.png")
    imgResized = image.resize((1120, 225))
    img = ImageTk.PhotoImage(imgResized)
    Label(guitarFrame, image=img, height=225, width=1120).place(x=0,y=0)

 

    # The Notes of a Guitar from the neck to the base (left to right)
    notes = [
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
        ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
    ]
    
    # Example list of note names in the same order as the notes (noteNames)
    noteNames = [['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
        ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']]

                

    # Create Labels for chord (chordLabel) and note indicators (notesLabel)
    chordLabel = Label(text="Chord: "); chordLabel.grid(row=7, column=1, columnspan=4, pady=10)
    notesLabel = Label(text="Notes: ", borderwidth=2, relief="solid"); notesLabel.grid(row=8, column=1, columnspan=4, pady=10)
    
    # Create 6 strings with 12 notes in each (allNotes)
    # Create integer values for notes (selectedNotes)
    # Create an Array to Store previous buttons pressed (pastSelectedNotes)

    # Create a list of IntVar() objects to represent the notes on the string
    for i, string in enumerate(allNotes):
        selectedNotes.append(IntVar())
        pastSelectedNotes[i] = 0
        for j, note in enumerate(string):
            
            print(j)
            newNote = Note(i, j, allNotes, notesLabel, selectedNotes[i],
                           selectedNotes, guitarFrame, pastSelectedNotes, noteNames[i][j])
            
            allNotes[i][j] = newNote
            newNote.button.grid(row=(i + 1), column=j, padx=30, pady=7)

    # Launch GUI
    window.mainloop()

def on_click(i, j, allNotes, notesLabel, selectedNoteIndex, pastSelectedNoteIndex):
    # Get the 2D array to which the clicked radio button belongs
    Radiobutton = allNotes[i][j]
    if pastSelectedNoteIndex[i] == j:
        selectedNoteIndex.set(-1)
        pastSelectedNoteIndex[i] = -1
    else:
        selectedNoteIndex.set(j)
        pastSelectedNoteIndex[i] = j
    
    # Create an Array to Store current note idexies from buttons pressed (currentSelectedNoteIndex)
    currentSelectedNoteIndex = []

    for stringIndex, noteIndex in enumerate(pastSelectedNoteIndex):
        if noteIndex != -1:
            currentSelectedNoteIndex.append((noteIndex, stringIndex))

    print("currentSelectedNoteIndex are: " + str(currentSelectedNoteIndex))

    currentNotes = getCurrentNote(allNotes, currentSelectedNoteIndex)
    currentNoteNames = [note.name for note in currentNotes]

    print(f"Clicked notes: {[f'{a, b}' for a, b in zip(currentSelectedNoteIndex, currentNoteNames)]}")
    # Updates a notesLabel text to the currentNoteNames
    notesLabel.config(text="Notes: " +", ".join(currentNoteNames))

class Note:
    def __init__(self, i, j, allNotes, notesLabel, int_var, selectedNotes, window, pastSelectedNotes, noteName):
        self.int_var = int_var
        self.name = noteName
        self.button = Radiobutton(window, variable=selectedNotes[i], value=j, command=lambda i=i, j=j: on_click(i, j, allNotes, notesLabel, int_var, pastSelectedNotes))


if __name__ == '__main__':
    main()