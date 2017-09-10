class Node:

    def __init__(self):
        self.next = None

    def __init__(self, initdata):
        self.data = initdata
        self.next = None


    def setData(self, data):
        self.data = data


    def setNext(self, next):
        self.next = next


    def getData(self):
        return self.data

    def getNext(self):
        return self.next