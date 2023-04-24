# Import necessary libraries
from tkinter import *
from note import Note


def main():
    # Create an instance of tkinter frame or window
    window = Tk()

    # Set the geometry of tkinter frame
    window.title("Fretboard Simulator")

    # Dictionary for note name look up by note position
    # 2D array of notes
    notes = [
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
        ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
        ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
    ]

    # List of note names in the same order as the notes
    note_names = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']

    # Create Label for title
    program_title = Label(text="Guitar Fretboard Simulator V1.0", font="Helvetica 18 bold")
    program_title.grid(row=0, column=2, columnspan=4, pady=15)

    # Create Labels for chord and note indicators
    chord_label = Label(text="Chord: ")
    chord_label.grid(row=7, column=1, columnspan=4, pady=10)
    notes_label = Label(text="Notes: ")
    notes_label.grid(row=8, column=1, columnspan=4, pady=10)

    # Create 6 strings with 12 notes in each
    all_notes = [[None] * 12] * 6

    # Create integer values for notes
    selected_notes = []

    # Create array to store previous buttons pressed
    previous_selected_notes = [0] * 6

    # Select and deselect notes
    for i, string in enumerate(all_notes):
        # Create a list of IntVar() objects to represent the notes on the string
        selected_notes.append(IntVar())
        # Create a parallel array for selected notes that
        # remembers which note was selected right before a button was pressed
        previous_selected_notes[i] = 0

        # Inner loop creates each note on the string
        for j, note in enumerate(string):
            # Create simple note object to organize note information
            # and handle click events with the window and int_var
            # and hold onto the radio button that it represents
            new_note = Note(i, j, all_notes, notes_label,
                            selected_notes[i], selected_notes,
                            window, previous_selected_notes, note_names[j])
            # Saved all notes ( and therefore all radio buttons ) to a 2d array
            all_notes[i][j] = new_note
            # The first radio button row is set to i + 1 to skip the title row
            new_note.button.grid(row=i + 1, column=j, padx=30, pady=4)

    # Launch GUI
    window.mainloop()


if __name__ == '__main__':
    main()
