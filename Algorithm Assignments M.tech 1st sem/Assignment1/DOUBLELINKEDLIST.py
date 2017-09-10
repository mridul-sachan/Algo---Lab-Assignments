from node2 import Node2
from operator import xor
import ctypes

class LinkList:

    def __init__(self):
        self.head = None



    def add(self, data):
        current = Node2()
        current.setData(data)
        #c_long_p = ctypes.
        temp = id(current) ^ 0
        print(temp)
        current.setNpx(temp)

        if self.head != None:
            t1 = self.head.getNpx() ^ 0
            print(t1)
            t = t1 ^ id(current)
            self.head.setNpx(t)

        self.head = current



    def traverse(self):
        current = self.head
        prev = None

        while current!=None:
            print(current.getData())
            t1 = id(prev) ^ current.getNpx()
            prev = current
            current = ctypes.cast(t1, ctypes.py_object)
            #current = ctypes.cast(id(t1), Node())
