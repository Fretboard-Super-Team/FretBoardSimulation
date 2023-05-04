# Import necessry libraries
from tkinter import *
from tkinter import ttk
import model_v1
import FretBoard
import ChordList

class FretboardSimulator:
    def __init__(self, lowest_notes):
        # Create an instance of tkinter frame or window
        self.board = model_v1.Fretboard(lowest_notes)
        self.window = Tk()

        # Set the geometry of tkinter frame
        #window.geometry("700x350")
        self.window.title("Fretboard Simulator")

        # Create Label for title
        self.program_title = Label(text="Guitar Fretboard Simulator V1.0", font="Helvetica 18 bold")
        self.program_title.grid(row=0, column=2, columnspan=4, pady=15)

        # Create Labels for chord and note indicators
        self.chord_label = Label(text="Chord: ")
        self.chord_label.grid(row=7, column=1, columnspan=4, pady=10)
        self.notes_label = Label(text="Notes: ")
        self.notes_label.grid(row=8, column=1, columnspan=4, pady=10)

        # create 6 strings with 12 notes in each
        self.all_notes = [[None for _ in range(12)] for _ in range(6)]

        # create integer values for notes
        self.selected_notes = []

        # create array to store previous buttons pressed
        self.previous_selected_notes = [-1 for _ in range(6)]

        for i, string in enumerate(self.board.all_notes()):
            # Create a list of IntVar() objects to represent the notes on the string
            # selected_notes.append([IntVar() for _ in range(len(string))])
            self.selected_notes.append(IntVar())
            self.previous_selected_notes[i] = 0
            for j, note in enumerate(string):
                id_number = f"{i}-{j}"  # create the ID number by combining the string index and note index
                print(j)
                self.all_notes[i][j] = \
                    Radiobutton(self.window,
                                variable=self.selected_notes[i],
                                value=j,
                                text=id_number,  # add the ID number as the text of the Radiobutton
                                command=lambda i=i, j=j:
                                self.on_click(i,
                                              j,
                                              self.all_notes,
                                              self.notes_label,
                                              self.selected_notes[i],
                                              self.previous_selected_notes))
                self.all_notes[i][j].grid(row=i + 1, column=j, padx=30, pady=4)
            self.previous_selected_notes[i] = -1
            self.selected_notes[i].set(-1)

        # Launch GUI
        self.window.mainloop()

    def on_click(self, i, j, all_notes, notes_label, selected_note_index, previous_selected_note_indices):
        # Get the 2D array to which the clicked radio button belongs
        radio_button = all_notes[i][j]
        
        if previous_selected_note_indices[i] == j:
            selected_note_index.set(-1)
            previous_selected_note_indices[i] = -1
        else:
            selected_note_index.set(j)
            previous_selected_note_indices[i] = j
        currently_selected_note_indices = []
        for string_index, note_index in enumerate(previous_selected_note_indices):
            if note_index != -1:
                currently_selected_note_indices.append(note_index)
            else:
                currently_selected_note_indices.append(None)
        
        print("currently_selected_note_indices are: "+str(currently_selected_note_indices))
        chord, note_names, note_indices = self.board.play_chord(currently_selected_note_indices)
        print(f"Clicked notes: {[f'{a, b}' for a, b in zip(currently_selected_note_indices, note_names)]}")
        notes_label.config(text="Notes: "+", ".join(note_names))
        
        
        # creating the list of note names that can be used to determine the chord in ChordList
        unique_note_names_list = list(set(note_names))
        unique_note_names_list.sort()
        print("A unique list of the selected notes"+str(unique_note_names_list))
        
        
        try:
            chord_name = ChordList.check_input_for_chords(unique_note_names_list)
            self.chord_label.config(text="Chord: " + chord_name)
            chord_found = True
        except:
            self.chord_label.config(text="""Not a valid chord! Select a note for each string, or use the drop down menu for chord recommendations.
                                    The simulator can map triads and simple 7th chords. It's possible your selected notes make a chord too complicated for the currect version!""")
               
            
            
if __name__ == '__main__':
    FretboardSimulator(["E", "B", "G", "D", "A", "E"])