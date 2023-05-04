### Hard Coded List of All Chord ###

import model_v1
import FretBoard
import FretboardSimulator

# All of the chord lists are in alphabetical order, so the user input can be easily sorted.
all_possible_chords = []

c_major = ['C', 'E', 'G']
all_possible_chords.append(c_major)
c_sharp_major = ['C#', 'F', 'G#'] # e# is enharmonically spelled
all_possible_chords.append(c_sharp_major)
d_major = ['A', 'D', 'F#']
all_possible_chords.append(d_major)
d_sharp_major = ['A#', 'D#', 'G'] # f## is enharmonically spelled
all_possible_chords.append(d_sharp_major)
e_major = ['B', 'E', 'G#',]
all_possible_chords.append(e_major)
f_major = ['A', 'C', 'F']
all_possible_chords.append(f_major)
f_sharp_major = ['A#', 'C#', 'F#']
all_possible_chords.append(f_sharp_major)
g_major = ['B', 'D', 'G']
all_possible_chords.append(g_major)
g_sharp_major = ['C', 'D#', 'G#']
all_possible_chords.append(g_sharp_major)
a_major = ['A', 'C#', 'E']
all_possible_chords.append(a_major)
a_sharp_major = ['A#', 'D', 'F']
all_possible_chords.append(a_sharp_major)
b_major = ['B', 'D#', 'F#']
all_possible_chords.append(b_major)

# Minor Triads #
c_minor = ['C', 'D#', 'G']
all_possible_chords.append(c_minor)
c_sharp_minor = ['C#', 'E', 'G#']
all_possible_chords.append(c_sharp_minor)
d_minor = ['A', 'D', 'F']
all_possible_chords.append(d_minor)
d_sharp_minor = ['A#', 'D#', 'F#']
all_possible_chords.append(d_sharp_minor)
e_minor = ['B', 'E', 'G',]
all_possible_chords.append(e_minor)
f_minor = ['C', 'F', 'G#']
all_possible_chords.append(f_minor)
f_sharp_minor = ['A', 'C#', 'F#']
all_possible_chords.append(f_sharp_minor)
g_minor = ['A#', 'D', 'G']
all_possible_chords.append(g_minor)
g_sharp_minor = ['B', 'D#', 'G#']
all_possible_chords.append(g_sharp_minor)
a_minor = ['A', 'C', 'E']
all_possible_chords.append(a_minor)
a_sharp_minor = ['A#', 'C#', 'F']
all_possible_chords.append(a_sharp_minor)
b_minor = ['B', 'D', 'F#']
all_possible_chords.append(b_minor)

# Diminished Triads #
c_dim = ['C', 'D#', 'F#']
all_possible_chords.append(c_dim)
c_sharp_dim = ['C#', 'E', 'G']
all_possible_chords.append(c_sharp_dim)
d_dim = ['D', 'F', 'G#']
all_possible_chords.append(d_dim)
d_sharp_dim = ['A', 'D#', 'F#']
all_possible_chords.append(d_sharp_dim)
e_dim = ['A#', 'E', 'G',]
all_possible_chords.append(e_dim)
f_dim = ['B', 'F', 'G#']
all_possible_chords.append(f_dim)
f_sharp_dim = ['A', 'C', 'F#']
all_possible_chords.append(f_sharp_dim)
g_dim = ['A#', 'C#', 'G']
all_possible_chords.append(g_dim)
g_sharp_dim = ['B', 'D', 'G#']
all_possible_chords.append(g_sharp_dim)
a_dim = ['A', 'C', 'D#']
all_possible_chords.append(a_dim)
a_sharp_dim = ['A#', 'C#', 'E']
all_possible_chords.append(a_sharp_dim)
b_dim = ['B', 'D', 'F']
all_possible_chords.append(b_dim)

# Augmented Triads #
# these triads can be enharmonically spelled.
c_aug = ['C', 'E', 'G#']    #also e_aug and g#_aug
all_possible_chords.append(c_aug)
c_sharp_aug = ['A', 'C#', 'F']    #also f_aug and a_aug
all_possible_chords.append(c_sharp_aug)
d_aug = ['A#', 'D', 'F#']    #also f#_aug and a#_aug
all_possible_chords.append(d_aug)
d_sharp_aug = ['B', 'D#', 'G']    #also g_aug and b_aug
all_possible_chords.append(d_sharp_aug)

# Major 7ths #
c_major_7 = ['B', 'C', 'E', 'G']
all_possible_chords.append(c_major_7)
c_sharp_major_7 = ['C', 'C#', 'F', 'G#']
all_possible_chords.append(c_sharp_major_7)
d_major_7 = ['A', 'C#', 'D', 'F#']
all_possible_chords.append(d_major_7)
d_sharp_major_7 = ['A#', 'D', 'D#', 'G']
all_possible_chords.append(d_sharp_major_7)
e_major_7 = ['B', 'D#', 'E', 'G#',]
all_possible_chords.append(e_major_7)
f_major_7 = ['A', 'C', 'E', 'F']
all_possible_chords.append(f_major_7)
f_sharp_major_7 = ['A#', 'C#', 'F', 'F#']
all_possible_chords.append(f_sharp_major_7)
g_major_7 = ['B', 'D', 'F#', 'G']
all_possible_chords.append(g_major_7)
g_sharp_major_7 = ['C', 'D#', 'G', 'G#']
all_possible_chords.append(g_sharp_major_7)
a_major_7 = ['A', 'C#', 'E', 'G#']
all_possible_chords.append(a_major_7)
a_sharp_major_7 = ['A', 'A#', 'D', 'F']
all_possible_chords.append(a_sharp_major_7)
b_major_7 = ['A#', 'B', 'D#', 'F#']
all_possible_chords.append(b_major_7)

# Minor 7ths #
c_minor_7 = ['A#', 'C', 'D#', 'G']
all_possible_chords.append(c_minor_7)
c_sharp_minor_7 = ['C#', 'B', 'E', 'G#']
all_possible_chords.append(c_sharp_minor_7)
d_minor_7 = ['A', 'C', 'D', 'F']
all_possible_chords.append(d_minor_7)
d_sharp_minor_7 = ['A#', 'C#', 'D#', 'F#']
all_possible_chords.append(d_sharp_minor_7)
e_minor_7 = ['B', 'D', 'E', 'G',]
all_possible_chords.append(e_minor_7)
f_minor_7 = ['C', ' D#', 'F', 'G#']
all_possible_chords.append(f_minor_7)
f_sharp_minor_7 = ['A', 'C#', 'E', 'F#']
all_possible_chords.append(f_sharp_minor_7)
g_minor_7 = ['A#', 'D', 'F', 'G']
all_possible_chords.append(g_minor_7)
g_sharp_minor_7 = ['B', 'D#', 'F#', 'G#']
all_possible_chords.append(g_sharp_minor_7)
a_minor_7 = ['A', 'C', 'E', 'G']
all_possible_chords.append(a_minor_7)
a_sharp_minor_7 = ['A#', 'C#', 'F', 'G#']
all_possible_chords.append(a_sharp_minor_7)
b_minor_7 = ['A', 'B', 'D', 'F#']
all_possible_chords.append(b_minor_7)

chordnameslist = []
chordnameslist.append("c_major")
chordnameslist.append("c_sharp_major")
chordnameslist.append("d_major")
chordnameslist.append("d_sharp_major")
chordnameslist.append("e_major")
chordnameslist.append("f_major")
chordnameslist.append("f_sharp_major")
chordnameslist.append("g_major")
chordnameslist.append("g_sharp_major")
chordnameslist.append("a_major")
chordnameslist.append("a_sharp_major")
chordnameslist.append("b_major")

class Chord:
    def __init__(self, chordname, notelist):
        self.chordname = chordname
        self.notelist = notelist

    def checkchord(self, input):
        if input ==  self.notelist:
            return self.chordname
        else :
            return

# Major Triads #



# Creating the class that will check the chords
class ChordList:

    def __init__(self):
        self.chordlist = [Chord() for i in enumerate(all_possible_chords)]
        for i, each in all_possible_chords:
            name = chordnameslist[i]
            self.chordlist[i] = Chord(each, name)

    def check_input_for_chords(self, input):
        for chord in self.chordlist:
            return chord.checkchord(input)





