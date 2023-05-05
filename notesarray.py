import circQueue

class notesarray(circQueue.circQueue):

    def __init__(self):
        self.notesqueue = circQueue.circQueue(12)

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
    
# def main():
#     array = notesarray()
#     array.create()
#     array.returnarray()
#     for each in array:
#         print(each)

# if __name__ == '__main__':
#     main()