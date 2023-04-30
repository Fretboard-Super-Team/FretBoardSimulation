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
        return self.notesqueue.get(pointer)

class stringclass():

    def __init__(self, root):
        self.root = root
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

    def emptystring(self):
        while (self.array):
            self.array.pop()
    
    def printqueue(self):
        print(self.array)

    def printref(self):
        print(self.ref.returnarray())

def get_current_notes(all_notes, currently_selected_note_indices):
    return [all_notes[i][j] for i, j in currently_selected_note_indices]

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

