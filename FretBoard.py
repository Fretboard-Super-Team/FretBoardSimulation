import pychord

# TODO - Translation - change these note names to be the correct names to match in the pychord library

notes = [
    'E2', 'F2', 'F#2/Gb2', 'G2', 'G#2/Ab2', 'A2', 'A#2/Bb2', 'B2',
    'C3', 'C#3/Db3', 'D3', 'D#3/Eb3', 'E3', 'F3', 'F#3/Gb3', 'G3',
    'G#3/Ab3', 'A3', 'A#3/Bb3', 'B3', 'C4', 'C#4/Db4', 'D4', 'D#4/Eb4',
    'E4', 'F4', 'F#4/Gb4', 'G4', 'G#4/Ab4', 'A4', 'A#4/Bb4', 'B4',
    'C5', 'C#5/Db5', 'D5', 'D#5/Eb5', 'E5', 'F5', 'F#5/Gb5', 'G5',
    'G#5/Ab5', 'A5', 'A#5/Bb5', 'B5', 'C6', 'C#6/Db6', 'D6', 'D#6/Eb6',
    'E6', 'F6', 'F#6/Gb6', 'G6', 'G#6/Ab6', 'A6', 'A#6/Bb6', 'B6',
    'C7', 'C#7/Db7', 'D7', 'D#7/Eb7', 'E7', 'F7', 'F#7/Gb7', 'G7'
]

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