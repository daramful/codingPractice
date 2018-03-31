# Python program to reverse a linked list 
# Time Complexity : O(n)
# Space Complexity : O(1)
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

    # O(n)
    # Function to reverse the linked list
    def reverse_n(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
         

    #O(N**2)
    def reverse_n2(self):
        _head = self.head
        temp = _head
        n = 0
        while temp is not None:
            n += 1
            temp = temp.next
        for i in range(0, n):
            x = _head
            for k in range(0, n-i-1):
                x = x.next
            print(x.data)


    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Given Linked List")
llist.printList()

llist.reverse_n()
print("\nReversed Linked List")
llist.printList()

print("\nn2 Linked List")
llist.reverse_n2()

print("\niterate")
llist.printList()
