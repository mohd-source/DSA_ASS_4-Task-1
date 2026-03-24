# ============================================
# Day: Day 2
# ============================================

# ============================================
# Question / Problem Statement:
# Write a program to:
# 1. Find the position of a given value
# 2. Count occurrences of a value in a list
#
# Example:
# Input List: 10 -> 20 -> 30 -> 20 -> 40 -> null
# Find Position of 30: 2
# Count Occurrences of 20: 2
# ============================================


# ============================================
# Program:
# ============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    # Find method
    def find(self, value):
        temp = self.head
        position = 0

        while temp:
            if temp.data == value:
                return position
            temp = temp.next
            position += 1

        return -1

    # Count occurrences
    def countOccurrences(self, value):
        temp = self.head
        count = 0

        while temp:
            if temp.data == value:
                count += 1
            temp = temp.next

        return count

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ============================================
# Output:
# ============================================

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(20)
ll.insert(40)

ll.display()

print("Find Position of 30:", ll.find(30))
print("Count Occurrences of 20:", ll.countOccurrences(20))