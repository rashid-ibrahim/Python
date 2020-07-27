"""
Problem Statement Found At: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
"""

def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    curr = 1
    temp = head

    while curr < position:
        temp = temp.next
        curr += 1

    temp.next = temp.next.next

    return head