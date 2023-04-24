# Import necessry libraries
from tkinter import *
from tkinter import ttk


# given i for the string index and j for the note index return a list of notes from the 2d array
def get_current_notes(all_notes, currently_selected_note_indices):
    return [all_notes[i][j] for i, j in currently_selected_note_indices]

def main():
    # Create an instance of tkinter frame or window
    window = Tk()

    # Set the geometry of tkinter frame
    #window.geometry("700x350")
    window.title("Fretboard Simulator")

    # Dictionary for note name look up by note position
    # Example 2D array of notes
    notes = [
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
        ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
        ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
    ]

    # Example list of note names in the same order as the notes
    note_names = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']

    # Create Label for title
    program_title = Label(text="Guitar Fretboard Simulator V1.0", font="Helvetica 18 bold")
    program_title.grid(row=0, column=2, columnspan=4, pady=15)

    # Create Labels for chord and note indicators
    chord_label = Label(text="Chord: ")
    chord_label.grid(row=7, column=1, columnspan=4, pady=10)
    notes_label = Label(text="Notes: ")
    notes_label.grid(row=8, column=1, columnspan=4, pady=10)

    # create 6 strings with 12 notes in each
    all_notes = [[None] * 12] * 6

    # create integer values for notes
    selected_notes = []

    # create array to store previous buttons pressed
    previous_selected_notes = [0] * 6

    for i, string in enumerate(all_notes):
        # Create a list of IntVar() objects to represent the notes on the string
        # selected_notes.append([IntVar() for _ in range(len(string))])
        selected_notes.append(IntVar())
        previous_selected_notes[i] = 0
        for j, note in enumerate(string):
            print(j)
            new_note = Note(i,
                            j,
                            all_notes,
                            notes_label,
                            selected_notes[i],
                            selected_notes,
                            window,
                            previous_selected_notes,
                            note_names[j])
            all_notes[i][j] = new_note
            new_note.button.grid(row=i + 1, column=j, padx=30, pady=4)

    # Launch GUI
    window.mainloop()

def on_click(i, j, all_notes, notes_label, selected_note_index, previous_selected_note_indices):
    # Get the 2D array to which the clicked radio button belongs
    radio_button = all_notes[i][j].button
    if previous_selected_note_indices[i] == j:
        selected_note_index.set(-1)
        previous_selected_note_indices[i] = -1
    else:
        selected_note_index.set(j)
        previous_selected_note_indices[i] = j
    currently_selected_note_indices = []
    for string_index, note_index in enumerate(previous_selected_note_indices):
        if note_index != -1:
            currently_selected_note_indices.append((note_index, string_index))
    print("currently_selected_note_indices are: "+str(currently_selected_note_indices))
    current_notes = get_current_notes(all_notes, currently_selected_note_indices)
    current_note_names = [note.name for note in current_notes]
    print(f"Clicked notes: {[f'{a, b}' for a, b in zip(currently_selected_note_indices, current_note_names)]}")
    notes_label.config(text="Notes: "+", ".join(current_note_names))
class Note:
    def __init__(self,
                 i,
                 j,
                 all_notes,
                 notes_label,
                 int_var,
                 selected_notes,
                 window,
                 previous_selected_notes,
                 note_name):
        # self.int_var =
        self.name = note_name
        self.button = Radiobutton(window,
                                  variable=selected_notes[i],
                                  value=j,
                                  command=lambda i=i, j=j: on_click(i,
                                                                    j,
                                                                    all_notes,
                                                                    notes_label,
                                                                    int_var,
                                                                    previous_selected_notes))

if __name__ == '__main__':
    main()