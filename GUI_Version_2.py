from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import model_v1

class Note:
    def __init__(self, i, j, allNotes, notesLabel, int_var, selectedNotes, guitarFrame, pastSelectedNotes, noteName):
        # self.int_var =
        self.name = noteName
        self.button = Radiobutton(guitarFrame, variable=selectedNotes[i], value=j, command=lambda i=i, j=j: getCurrentNote(i, j, allNotes, notesLabel, int_var, pastSelectedNotes))

# given i for the string index and j for the note index return a list of notes from the 2d array
def getCurrentNote(allNotes, currentSelectedNoteIndex):
    return [allNotes[i][j] for i, j in currentSelectedNoteIndex]

def main():

    root = Tk()
    root.title("Fretboard Simulator V2")
    root.geometry("1220x450")

    # Creating Fretboard Label Widget (fretBoardTitle)
    fretBoardTitle = Label(root, text='FretBoard Simulation Version 2.0', borderwidth=2, relief="solid", font=("Times", "18", "bold"))
    fretBoardTitle.grid(row=0, column=0, columnspan=4, pady=15)

    # Created a quit button
    quitbtn = Button(root, text="Quit", font=("Times", "15", "bold"), borderwidth=2, relief="solid", command=root.destroy); quitbtn.grid(column=6, row=0)

    # Creating the Guitar Neck Frame (guitarFrame)
    guitarFrame = Frame(root, width=1120, height=225)
    guitarFrame.grid(row=1, column=0, columnspan=4, pady=15)
    guitarFrame.configure(background='#0ee0c7', relief="solid")
    
    # Not sure what to do with these?
    allNotes = [[None] * 12] * 6
    selectedNotes = []
    pastSelectedNotes = [0] * 6

    # BackRound Image
    image = Image.open("colored.png")
    imgResized = image.resize((1120, 225))
    img = ImageTk.PhotoImage(imgResized)
    Label(guitarFrame, image=img, height=225, width=1120).place(x=0,y=0)

    # Updates Notes Label to Selected variables on each String
    def printResults():
        txt = str(var1.get()) + ", " + str(var2.get()) + ", " + str(var3.get()) + ", " + str(var4.get()) + ", " + str(var5.get()) + ", " + str(var6.get())
        notesLabel.config(text = "Notes: " + txt)

    # This is each variable for all 6 strings
    var1 = StringVar(root); var2 = StringVar(root); var3 = StringVar(root)
    var4 = StringVar(root); var5 = StringVar(root); var6 = StringVar(root)

    # Open Strings 1-6 and Fret 0
    s1f0 = Radiobutton(guitarFrame, variable=var1, value="E", command=printResults); s1f0.grid(row=0, column=0, padx=10, pady=4)
    s2f0 = Radiobutton(guitarFrame, variable=var2, value="A", command=printResults); s2f0.grid(row=1, column=0, padx=10, pady=8)
    s3f0 = Radiobutton(guitarFrame, variable=var3, value="D", command=printResults); s3f0.grid(row=2, column=0, padx=10, pady=8)
    s4f0 = Radiobutton(guitarFrame, variable=var4, value="G", command=printResults); s4f0.grid(row=3, column=0, padx=10, pady=7)
    s5f0 = Radiobutton(guitarFrame, variable=var5, value="B", command=printResults); s5f0.grid(row=4, column=0, padx=10, pady=8)
    s6f0 = Radiobutton(guitarFrame, variable=var6, value="E", command=printResults); s6f0.grid(row=5, column=0, padx=10, pady=8)

    # Strings 1-6 and Fret 1
    s1f1 = Radiobutton(guitarFrame, variable=var1, value="F", command=printResults); s1f1.grid(row=0, column=1, padx=46, pady=5)
    s2f1 = Radiobutton(guitarFrame, variable=var2, value="A#", command=printResults); s2f1.grid(row=1, column=1, padx=46, pady=5)
    s3f1 = Radiobutton(guitarFrame, variable=var3, value="D#", command=printResults); s3f1.grid(row=2, column=1, padx=46, pady=5)
    s4f1 = Radiobutton(guitarFrame, variable=var4, value="G#", command=printResults); s4f1.grid(row=3, column=1, padx=46, pady=5)
    s5f1 = Radiobutton(guitarFrame, variable=var5, value="C", command=printResults); s5f1.grid(row=4, column=1, padx=46, pady=5)
    s6f1 = Radiobutton(guitarFrame, variable=var6, value="F", command=printResults); s6f1.grid(row=5, column=1, padx=46, pady=5)

    # Strings 1-6 and Fret 2
    s1f2 = Radiobutton(guitarFrame, variable=var1, value="F#", command=printResults); s1f2.grid(row=0, column=2, padx=19, pady=4)
    s2f2 = Radiobutton(guitarFrame, variable=var2, value="B", command=printResults); s2f2.grid(row=1, column=2, padx=19, pady=4)
    s3f2 = Radiobutton(guitarFrame, variable=var3, value="E", command=printResults); s3f2.grid(row=2, column=2, padx=19, pady=4)
    s4f2 = Radiobutton(guitarFrame, variable=var4, value="A", command=printResults); s4f2.grid(row=3, column=2, padx=19, pady=4)
    s5f2 = Radiobutton(guitarFrame, variable=var5, value="C#", command=printResults); s5f2.grid(row=4, column=2, padx=19, pady=4)
    s6f2 = Radiobutton(guitarFrame, variable=var6, value="F#", command=printResults); s6f2.grid(row=5, column=2, padx=19, pady=4)

    # Strings 1-6 and Fret 3
    s1f3 = Radiobutton(guitarFrame, variable=var1, value="G", command=printResults); s1f3.grid(row=0, column=3, padx=43, pady=4)
    s2f3 = Radiobutton(guitarFrame, variable=var2, value="C", command=printResults); s2f3.grid(row=1, column=3, padx=43, pady=4)
    s3f3 = Radiobutton(guitarFrame, variable=var3, value="F", command=printResults); s3f3.grid(row=2, column=3, padx=43, pady=4)
    s4f3 = Radiobutton(guitarFrame, variable=var4, value="A#", command=printResults); s4f3.grid(row=3, column=3, padx=43, pady=4)
    s5f3 = Radiobutton(guitarFrame, variable=var5, value="D", command=printResults); s5f3.grid(row=4, column=3, padx=43, pady=4)
    s6f3 = Radiobutton(guitarFrame, variable=var6, value="G", command=printResults); s6f3.grid(row=5, column=3, padx=43, pady=4)

    # Strings 1-6 and Fret 4
    s1f4 = Radiobutton(guitarFrame, variable=var1, value="G#", command=printResults); s1f4.grid(row=0, column=4, padx=22, pady=4)
    s2f4 = Radiobutton(guitarFrame, variable=var2, value="C#", command=printResults); s2f4.grid(row=1, column=4, padx=22, pady=4)
    s3f4 = Radiobutton(guitarFrame, variable=var3, value="F#", command=printResults); s3f4.grid(row=2, column=4, padx=22, pady=4)
    s4f4 = Radiobutton(guitarFrame, variable=var4, value="B", command=printResults); s4f4.grid(row=3, column=4, padx=22, pady=4)
    s5f4 = Radiobutton(guitarFrame, variable=var5, value="D#", command=printResults); s5f4.grid(row=4, column=4, padx=22, pady=4)
    s6f4 = Radiobutton(guitarFrame, variable=var6, value="G#", command=printResults); s6f4.grid(row=5, column=4, padx=22, pady=4)
    
    # Strings 1-6 and Fret 5
    s1f5 = Radiobutton(guitarFrame, variable=var1, value="A", command=printResults); s1f5.grid(row=0, column=5, padx=42, pady=4)
    s2f5 = Radiobutton(guitarFrame, variable=var2, value="D", command=printResults); s2f5.grid(row=1, column=5, padx=42, pady=4)
    s3f5 = Radiobutton(guitarFrame, variable=var3, value="G", command=printResults); s3f5.grid(row=2, column=5, padx=42, pady=4)
    s4f5 = Radiobutton(guitarFrame, variable=var4, value="C", command=printResults); s4f5.grid(row=3, column=5, padx=42, pady=4)
    s5f5 = Radiobutton(guitarFrame, variable=var5, value="E", command=printResults); s5f5.grid(row=4, column=5, padx=42, pady=4)
    s6f5 = Radiobutton(guitarFrame, variable=var6, value="A", command=printResults); s6f5.grid(row=5, column=5, padx=42, pady=4)

    # Strings 1-6 and Fret 6
    s1f6 = Radiobutton(guitarFrame, variable=var1, value="A#", command=printResults); s1f6.grid(row=0, column=6, padx=22, pady=4)
    s2f6 = Radiobutton(guitarFrame, variable=var2, value="D#", command=printResults); s2f6.grid(row=1, column=6, padx=22, pady=4)
    s3f6 = Radiobutton(guitarFrame, variable=var3, value="G#", command=printResults); s3f6.grid(row=2, column=6, padx=22, pady=4)
    s4f6 = Radiobutton(guitarFrame, variable=var4, value="C#", command=printResults); s4f6.grid(row=3, column=6, padx=22, pady=4)
    s5f6 = Radiobutton(guitarFrame, variable=var5, value="F", command=printResults); s5f6.grid(row=4, column=6, padx=22, pady=4)
    s6f6 = Radiobutton(guitarFrame, variable=var6, value="A#", command=printResults); s6f6.grid(row=5, column=6, padx=22, pady=4)

    # Strings 1-6 and Fret 7
    s1f7 = Radiobutton(guitarFrame, variable=var1, value="B", command=printResults); s1f7.grid(row=0, column=7, padx=41, pady=4)
    s2f7 = Radiobutton(guitarFrame, variable=var2, value="E", command=printResults); s2f7.grid(row=1, column=7, padx=41, pady=4)
    s3f7 = Radiobutton(guitarFrame, variable=var3, value="A", command=printResults); s3f7.grid(row=2, column=7, padx=41, pady=4)
    s4f7 = Radiobutton(guitarFrame, variable=var4, value="D", command=printResults); s4f7.grid(row=3, column=7, padx=41, pady=4)
    s5f7 = Radiobutton(guitarFrame, variable=var5, value="F#", command=printResults); s5f7.grid(row=4, column=7, padx=41, pady=4)
    s6f7 = Radiobutton(guitarFrame, variable=var6, value="B", command=printResults); s6f7.grid(row=5, column=7, padx=41, pady=4)

    # Strings 1-6 and Fret 8
    s1f8 = Radiobutton(guitarFrame, variable=var1, value="C", command=printResults); s1f8.grid(row=0, column=8, padx=23, pady=4)
    s2f8 = Radiobutton(guitarFrame, variable=var2, value="F", command=printResults); s2f8.grid(row=1, column=8, padx=23, pady=4)
    s3f8 = Radiobutton(guitarFrame, variable=var3, value="A#", command=printResults); s3f8.grid(row=2, column=8, padx=23, pady=4)
    s4f8 = Radiobutton(guitarFrame, variable=var4, value="D#", command=printResults); s4f8.grid(row=3, column=8, padx=23, pady=4)
    s5f8 = Radiobutton(guitarFrame, variable=var5, value="G", command=printResults); s5f8.grid(row=4, column=8, padx=23, pady=4)
    s6f8 = Radiobutton(guitarFrame, variable=var6, value="C", command=printResults); s6f8.grid(row=5, column=8, padx=23, pady=4)

    # Strings 1-6 and Fret 9
    s1f9 = Radiobutton(guitarFrame, variable=var1, value="C#", command=printResults); s1f9.grid(row=0, column=9, padx=41, pady=4)
    s2f9 = Radiobutton(guitarFrame, variable=var2, value="F#", command=printResults); s2f9.grid(row=1, column=9, padx=41, pady=4)
    s3f9 = Radiobutton(guitarFrame, variable=var3, value="B", command=printResults); s3f9.grid(row=2, column=9, padx=41, pady=4)
    s4f9 = Radiobutton(guitarFrame, variable=var4, value="E", command=printResults); s4f9.grid(row=3, column=9, padx=41, pady=4)
    s5f9 = Radiobutton(guitarFrame, variable=var5, value="G#", command=printResults); s5f9.grid(row=4, column=9, padx=41, pady=4)
    s6f9 = Radiobutton(guitarFrame, variable=var6, value="C#", command=printResults); s6f9.grid(row=5, column=9, padx=41, pady=4)

    # Strings 1-6 and Fret 10
    s1f10 = Radiobutton(guitarFrame, variable=var1, value="D", command=printResults); s1f10.grid(row=0, column=10, padx=23, pady=4)
    s2f10 = Radiobutton(guitarFrame, variable=var2, value="G", command=printResults); s2f10.grid(row=1, column=10, padx=23, pady=4)
    s3f10 = Radiobutton(guitarFrame, variable=var3, value="C", command=printResults); s3f10.grid(row=2, column=10, padx=23, pady=4)
    s4f10 = Radiobutton(guitarFrame, variable=var4, value="F", command=printResults); s4f10.grid(row=3, column=10, padx=23, pady=4)
    s5f10 = Radiobutton(guitarFrame, variable=var5, value="A", command=printResults); s5f10.grid(row=4, column=10, padx=23, pady=4)
    s6f10 = Radiobutton(guitarFrame, variable=var6, value="D", command=printResults); s6f10.grid(row=5, column=10, padx=23, pady=4)

    # Strings 1-6 and Fret 11
    s1f11 = Radiobutton(guitarFrame, variable=var1, value="D#", command=printResults); s1f11.grid(row=0, column=11, padx=41, pady=4)
    s2f11 = Radiobutton(guitarFrame, variable=var2, value="G#", command=printResults); s2f11.grid(row=1, column=11, padx=41, pady=4)
    s3f11 = Radiobutton(guitarFrame, variable=var3, value="C#", command=printResults); s3f11.grid(row=2, column=11, padx=41, pady=4)
    s4f11 = Radiobutton(guitarFrame, variable=var4, value="F#", command=printResults); s4f11.grid(row=3, column=11, padx=41, pady=4)
    s5f11 = Radiobutton(guitarFrame, variable=var5, value="A#", command=printResults); s5f11.grid(row=4, column=11, padx=41, pady=4)
    s6f11 = Radiobutton(guitarFrame, variable=var6, value="D#", command=printResults); s6f11.grid(row=5, column=11, padx=41, pady=4)


    notes = [
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'], ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'], ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'], ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
    ]

    
    musicFrame = Frame(root, borderwidth=2, relief="solid", padx=30); musicFrame.grid(row=3, column=0)

    notesLabel = Label(musicFrame, text="Notes: ", font=("Times", "13", "bold")); notesLabel.grid(row=7, column=1, columnspan=4, pady=10)
    chordLabel = Label(musicFrame, text="Chord: ", font=("Times", "13", "bold")); chordLabel.grid(row=8, column=1, columnspan=4, pady=10)
    
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    chords_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Chords", menu=chords_menu)

    major_menu = Menu(chords_menu, tearoff=0)
    chords_menu.add_cascade(label="Major Chords", menu=major_menu)

    major_menu.add_command(label="A")
    major_menu.add_command(label="B")
    major_menu.add_command(label="C")
    major_menu.add_command(label="D")
    major_menu.add_command(label="E")
    major_menu.add_command(label="F")
    major_menu.add_command(label="G")

    minor_menu = Menu(chords_menu, tearoff=0)
    chords_menu.add_cascade(label="Minor Chords", menu=minor_menu)

    minor_menu.add_command(label="Am")
    minor_menu.add_command(label="Bm")
    minor_menu.add_command(label="Cm")
    minor_menu.add_command(label="Dm")
    minor_menu.add_command(label="Em")
    minor_menu.add_command(label="Fm")
    minor_menu.add_command(label="Gm")
    
    root.mainloop()


if __name__ == '__main__':
    main()
   