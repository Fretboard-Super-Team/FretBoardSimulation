from model_v1 import *
import FretboardSimulator
import ChordList

# TODO - Translation - change these note names to be the correct names to match in the pychord library

notes = ['F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C1', 'C#1', 'D1', 'D#1',
         'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2',
         'G#3', 'A3', 'A#3', 'B3', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3',
         'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4' , 'A#4', 'B4', 'C4', 'C#4',
         'A#5', 'B5', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5',
         'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C6', 'C#6', 'D6', 'D#6']

# Major Chords

majors = [[notes[2], 'C#2', 'A3', 'E4', 'A0', 'E0L'],
          ['F#1', 'D#2', 'B3', 'F#4', 'B5', 'F#6'],
          ['E0H', 'C2', 'G0', 'E4', 'C5', 'E0L'],
          ['F#1', 'D2', 'A3', 'D0', 'A0', 'E0L'],
          ['E0H', 'B0', 'G#3', 'E4', 'B5', 'E0L'],
          ['F1', 'C2', 'A3', 'F4', 'C5', 'F6'],
          ['G1', 'B0', 'G0', 'D0', 'B5', 'G6']]

A = ['EH', 'C#2', '']

minors = [['E0H', 'C2', 'A3', 'E4', 'A0', 'E0L'],
          ['F#1', 'D2', 'B3', 'F#4', 'B5', 'F#6'],
          ['G1', 'D#2', 'C3', 'G4', 'C5', 'G6'],
          ['F1', 'D2', 'A3', 'D0', 'A0', 'E0L'],
          ['E0H', 'B0', 'G0', 'E4', 'B5', 'E0L'],
          ['F1', 'C2', 'G#3', 'F4', 'C5', 'F6'],
          ['G1', 'D2', 'A#3', 'G4', 'D5', 'G6']]

number_of_strings = 6
notes_per_string = 12


class Fretboard:
    def __init__(self,
                 desired_tunings):
        self.lowest_notes = [None for _ in range(number_of_strings)]
        for i, lowest_note in enumerate(desired_tunings):
            self.change_guitar_tuning(i, lowest_note)

    def change_guitar_tuning(self, string_index, new_lowest_note):
        if new_lowest_note < 0 or new_lowest_note > len(notes) - 12:
            print(f"Error: Invalid new lowest note {new_lowest_note}")
            exit(1)
        self.lowest_notes[string_index] = new_lowest_note

    def play_chord(self, notes_list):
        note_names = []
        note_indices = []
        # note_index is an index that tells us what number between 0 and 11 has been selected
        for i, note_index in enumerate(notes_list):
            if note_index is None:
                continue
            # i is the string index
            # multiplied by 12 each loop to get the correct offset for that string, gives 1st note in each string
            # To get specific note add note_index
            index = i * notes_per_string + note_index
            note_indices.append(index)
            # list of corresponding note names based on mapping note indices list to notes list
            # collect notes into the note_names list using append
            note_names.append(notes[index])
        print(note_names)

        # TODO - TRANSLATION
        # Feed note_names list into pychord package to return chord name
        # chord = pychord.find_chords_from_notes(note_names)
        # print(chord, note_names, note_indices)
        return None, note_names, note_indices
        # get rid of line above and replace with line below once chords and notes are translated correctly using pychord
        # return chord, note_names, note_indices

    # this list comprehension returns the two dimensional list of notes representing the current tuning
    def all_notes(self):
        all_notes = []
        for i, lowest_note_index in enumerate(self.lowest_notes):
            string = []
            for j in range(notes_per_string):
                string.append(notes[lowest_note_index + j])
            all_notes.append(string)
        return all_notes