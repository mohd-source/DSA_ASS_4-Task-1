# ============================================
# Day: Day 1
# ============================================

# ============================================
# Question / Problem Statement:
# Write a program to insert a node at a specific
# position in a doubly linked list.
#
# Example:
# Input List: 10 -> 20 -> 40 -> null
# Insert 30 at position 2
# Output: 10 -> 20 -> 30 -> 40 -> null
# ============================================


# ============================================
# Program:
# ============================================

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)

        # Insert at beginning
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        count = 0

        # Traverse to correct position
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        # Adjust pointers
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")



dll = DoublyLinkedList()

dll.insert_at_position(10, 0)
dll.insert_at_position(20, 1)
dll.insert_at_position(40, 2)

print("Input List:")
dll.display()

dll.insert_at_position(30, 2)

print("After inserting 30 at position 2:")
dll.display()