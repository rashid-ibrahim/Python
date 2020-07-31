"""
Problem Statement found at: https://www.hackerrank.com/challenges/30-linked-list/problem
"""


# ####Begin Auto Generated Code####
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # ####End Auto Generated Code####

        if not head:
            return Node(data)

        temp = head

        while True:
            if not temp.next:
                break
            temp = temp.next

        temp.next = Node(data)

        return head