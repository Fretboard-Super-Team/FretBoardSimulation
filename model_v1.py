from tkinter import *

class circQueue(list):

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.end = self.pointer = -1
        self.index = list.index

    def enqueue(self, element):
        if ((self.end  + 1) % self.size == self.front):
            print("Queue is full")

        elif (self.end == -1):
            self.end = 0
            self.front = 0
            self.queue[self.end] = element

        else: 
            self.end = (self.end + 1) % self.size
            self.queue[self.end] = element

    def dequeue(self):
        if (self.front == -1):
            print("Queue is empty")

        elif (self.front == self.end):
            temp = self.queue[self.front]
            self.front = -1
            self.end = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
        
    def get(self, pointer):
        if pointer >= len(self.queue):
            pointer %= len(self.queue)
        return self.queue[pointer]

class notesarray(circQueue):

    def __init__(self):
        self.notesqueue = circQueue(12)

    def create(self):
        self.notesqueue.enqueue("A")
        self.notesqueue.enqueue("A#")
        self.notesqueue.enqueue("B")
        self.notesqueue.enqueue("C")
        self.notesqueue.enqueue("C#")
        self.notesqueue.enqueue("D")
        self.notesqueue.enqueue("D#")
        self.notesqueue.enqueue("E")
        self.notesqueue.enqueue("F")
        self.notesqueue.enqueue("F#")
        self.notesqueue.enqueue("G")
        self.notesqueue.enqueue("G#")
    
    def returnarray(self):
        return self.notesqueue.queue
    
    def get(self, pointer):
        note = self.notesqueue.get(pointer)
        return note

class stringclass():

    def __init__(self):
        #self.root = root
        self.array = [] * 12
        self.ref = notesarray()
        self.ref.create()

    def setroot(self, newroot):
        self.root = newroot
    
    def fillnotes(self):
        i = self.ref.returnarray().index(self.root)
        while True:
            self.array.append(self.ref.get(i))
            i = i + 1
            if (self.ref.get(i) == self.root):
                break

    def returnnote(self, index):
        return self.array[index]
    
    def emptystring(self):
        while (self.array):
            self.array.pop()
    
    def printnotes(self):
        print(self.array)
        return self.array

    def printref(self):
        print(self.ref.returnarray())

def get_current_notes(all_notes, currently_selected_note_indices):
    return [all_notes[i][j] for i, j in currently_selected_note_indices]

# TODO - Translation - change these note names to be the correct names to match in the pychord library

number_of_strings = 6

class Fretboard:
    def __init__(self,
                 desired_tunings):
        self.strings = [stringclass() for i in range(number_of_strings)]
        for i, each in enumerate(desired_tunings):
            self.strings[i].setroot(each)
            self.strings[i].fillnotes()

    def returnstrings(self, strnum):
        return self.strings[strnum]


    def play_chord(self, notes_list):
        note_names = []
        note_indices = []
        # note_index is an index that tells us what number between 0 and 11 has been selected
        for i, note_index in enumerate(notes_list):
            if note_index is None:
                continue
            # i is the string index
            note_indices.append(self.strings[i].returnnote(note_index).index)
            # list of corresponding note names based on mapping note indices list to notes list
            # collect notes into the note_names list using append
            note_names.append(self.strings[i].returnnote(note_index))
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
        for each in self.strings:
            all_notes.append(each.printnotes())
        return all_notes

