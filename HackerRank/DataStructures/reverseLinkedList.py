"""
Problem Statement at: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
"""


def reverse(head):
    prev, next = None, None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next

    head = prev

    return head
