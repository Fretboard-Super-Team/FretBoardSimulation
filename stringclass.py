import circQueue
import notesarray

class stringclass():

    def __init__(self, root):
        self.root = root
        self.array = [] * 12
        self.ref = notesarray.notesarray()
        self.ref.create()

    def printref(self):
        print(self.ref.returnarray())
    
    def fillnotes(self):
        i = self.ref.returnarray().index(self.root)
        while True:
            self.array.append(self.ref.get(i))
            i = i + 1
            if (self.ref.get(i) == self.root):
                break
    
    def printqueue(self):
        print(self.array)

# def main():
#     teststring = stringclass("E")
#     print("Testing ref:")
#     teststring.printref()
#     print("Testing empty q:")
#     teststring.printqueue()
#     print("Testing filling notes:")
#     teststring.fillnotes()
#     print("Testing filled q:")
#     teststring.printqueue()

# if __name__ == '__main__':
#     main()
