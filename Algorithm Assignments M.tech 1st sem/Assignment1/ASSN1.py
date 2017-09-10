from stack import Stack
from queue import Queue
from list import List
from doublylinkedlist import LinkList


# Queue using 2 Stacks
def queue_using_stack():
    s1 = Stack()
    s2 = Stack()
    choice = 1
    while(choice!=0):
        print("1. Enqueue")
        print("2. Dequeue")
        choice = int(input(">"))

        if choice == 1:
            continue_add = 'y'
            while(continue_add != 'n'):
                s1.push(input("Enter the element: "))
                continue_add = input("Continue (y/n): ")



        elif choice == 2:
            if not s1.isEmpty():
                for t in range(0, s1.size()):
                    v = s1.pop()
                    s2.push(v)

                print("The popped element is: {}".format(s2.pop()))
                for t in range(0, s2.size()):
                    v = s2.pop()
                    s1.push(v)


            else:
                print("Stack empty")




# Stack using Queue
def stack_using_queue():
    q1 = Queue()
    q2 = Queue()
    choice = 1
    while(choice!=0):
        print("1. Push")
        print("2. Pop")
        choice = int(input(">"))

        if choice == 1:
            continue_add = 'y'
            while(continue_add != 'n'):
                q1.enqueue(input("Enter the item: "))
                continue_add = input("Continue (y/n): ")



        elif choice == 2:
            if not q1.isEmpty():
                for k in range(0, q1.size() - 1):
                    q2.enqueue(q1.dequeue())

                print("The popped element is: {}".format(q1.dequeue()))

                for t in range(0, q2.size()):
                    q1.enqueue(q2.dequeue())

            else:
                print("Queue empty")

    


# Stack using Singly Link List
def stack_using_linklist():
    list = List()
    choice = 1
    while choice != 0:
        print("1. Push")
        print("2. Pop")
        print("3. Top")
        choice = int(input(">"))

        if choice == 1:
            continue_add = 'y'
            while continue_add != 'n':
                list.add(input("Enter the element: "))
                continue_add = input("Continue (y/n): ")


            print("\nThe List is: ", list.print(),"\n")


        elif choice == 2:
            if not list.isEmpty():
                print("\nThe popped element is: ", list.remove())
                print("The List now is: ", list.print(), "\n")

            else:
                print("Stack empty")

        elif choice == 3:
            if not list.isEmpty():
                print("\nThe top element is: ", list.printTop())

            else:
                print("Stack empty")





# Queue using Singly Linked List
def queue_from_linklist():
    list = List()
    choice = 1
    while choice != 0:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        choice = int(input(">"))

        if choice == 1:
            continue_add = 'y'
            while continue_add != 'n':
                list.add2(input("Enter the element: "))
                continue_add = input("Continue (y/n): ")



        elif choice == 2:
            if not list.isEmpty():
                print("\nThe dequeued element is: ", list.remove2())

            else:
                print("Queue empty")


        elif choice == 3:
            if not list.isEmpty():
                print("\nThe front element is: ", list.printFront())

            else:
                print("Queue empty")





def doubly_linked_list():
    linkLlist = LinkList()
    linkLlist.add(54)
    linkLlist.add(89)
    linkLlist.add(33)
    linkLlist.add(23)

    linkLlist.traverse()





# Driver Function
if __name__ == "__main__":

    print("="*50)
    print(" "*22,"Menu"," "*22)
    print("="*50)
    print("1. Queue using 2 Stacks")
    print("2. Stack using 2 Queues")
    print("3. Stack using Singly Linked List")
    print("4. Queue using Singly Linked List")
    print("5. Doubly Linked List")
    choice = int(input(">"))

    if choice == 1:
        queue_using_stack()

    elif choice == 2:
        stack_using_queue()

    elif choice == 3:
        stack_using_linklist()

    elif choice == 4:
        queue_from_linklist()

    elif choice == 5:
        doubly_linked_list()



        
