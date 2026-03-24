# ============================================
# Day: Day 3
# ============================================

# ============================================
# Question / Problem Statement:
# Write a program to sort a doubly linked list
# in ascending order using Bubble Sort.
# Sorting must be done by rearranging pointers
# (next and prev), NOT by swapping data.
#
# Example:
# Input:  40 -> 20 -> 30 -> 10 -> null
# Output: 10 -> 20 -> 30 -> 40 -> null
# ============================================


# ============================================
# Program:
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Swap adjacent nodes
    def swap(self, node1, node2):
        if node1.prev:
            node1.prev.next = node2
        else:
            self.head = node2

        if node2.next:
            node2.next.prev = node1

        node1.next = node2.next
        node2.prev = node1.prev

        node2.next = node1
        node1.prev = node2

    # Bubble Sort
    def sort(self):
        if self.head is None:
            return

        swapped = True

        while swapped:
            swapped = False
            temp = self.head

            while temp and temp.next:
                if temp.data > temp.next.data:
                    self.swap(temp, temp.next)
                    swapped = True

                    if temp.prev:
                        temp = temp.prev
                else:
                    temp = temp.next


# ============================================
# Output:
# ============================================

dll = DoublyLinkedList()

dll.insert(40)
dll.insert(20)
dll.insert(30)
dll.insert(10)

print("Input List:")
dll.display()

dll.sort()

print("Sorted List:")
dll.display()