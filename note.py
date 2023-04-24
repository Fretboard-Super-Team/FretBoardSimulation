from tkinter import *

class Note:
    def __init__(self, i, j, all_notes,
                 notes_label, int_var,
                 selected_notes, window,
                 previous_selected_notes, note_name):
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


def on_click(i, j, all_notes, notes_label, selected_note_index, previous_selected_note_indices):
    # Check if the clicked note is already selected
    # if so, deselect it (by setting the index to -1)
    if previous_selected_note_indices[i] == j:
        selected_note_index.set(-1)
        previous_selected_note_indices[i] = -1
    # Otherwise, select note as usual
    else:
        selected_note_index.set(j)
        previous_selected_note_indices[i] = j
    # Place all currently selected note positions into an array
    currently_selected_note_indices = [(note_index, string_index)
                                       for string_index, note_index in enumerate(previous_selected_note_indices)
                                       if note_index != -1]

    # Print the currently selected note indices
    print(f"currently_selected_note_indices are: {currently_selected_note_indices}")

    # Get the current notes based on their indices
    current_notes = get_current_notes(all_notes, currently_selected_note_indices)

    # Get the current note names from their Note objects
    current_note_names = [note.name for note in current_notes]
    print(f"Clicked notes: {[f'{a, b}' for a, b in zip(currently_selected_note_indices, current_note_names)]}")

    # Update 'Notes:' label with currently selected note names
    notes_label.config(text="Notes: " + ", ".join(current_note_names))


# given i for the string index and j for the note index return a list of notes from the 2d array
def get_current_notes(all_notes, currently_selected_note_indices):
    return [all_notes[i][j] for i, j in currently_selected_note_indices]
