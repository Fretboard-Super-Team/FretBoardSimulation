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


# def main():
#         testq = circQueue(3)
#         testq.enqueue("A")
#         testq.enqueue("B")
#         testq.enqueue("C")
#         print(testq.get(0))
#         print(testq.get(1))
#         print(testq.get(2))

# if __name__ == '__main__':
#     main()
        
