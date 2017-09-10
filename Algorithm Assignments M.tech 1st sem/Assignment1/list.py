from node import Node

class List:
    def __init__(self):
        self.head = None
        self.front = None
        self.rear = None


    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp



    def add2(self, item):
        temp = Node(item)
        temp.setNext(None)
        if self.front == None and self.rear == None:
            self.front = temp
            self.rear = temp

        else:
            self.rear.setNext(temp)
            self.rear = temp




    def printTop(self):
        return self.head.getData()


    def printFront(self):
        return self.front.getData()


    def print(self):
        current = self.head
        op = "";
        while current!=None:
            op += current.getData() + " "
            current = current.getNext()

        return op


    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            tt = current.getData()
            if tt == item:
                found = True

            else:
                current = current.getNext()

        return found



    def get(self, index):
        current = self.head
        val = -1
        count = 0
        print(index)
        while current != None:
            count+=1
            if count == index:
                val = current.getData()
            else:
                current = current.getNext()

        return val



    def indexof(self, item):
        current = self.head
        index = 0
        while current!=None:
            if current.getData() == item:
                index+=1
                return index
            else:
                current = current.getNext()




    def remove(self):
        current = self.head
        val = current.getData()
        self.head = current.getNext()

        return val



    def remove2(self):
        current = self.front
        val = current.getData()
        if self.front == None:
            return

        elif self.front == self.rear:
            self.front = None
            self.rear = None
            return val

        else:
            self.front = self.front.getNext()
            return val






    def isEmpty(self):
        return self.head == None


    def size(self):
        count = 0
        current = self.head
        while current != None:
            count+=1
            current = current.getNext()

        return count