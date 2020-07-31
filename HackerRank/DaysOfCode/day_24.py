"""
Problem Statement At: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
"""


# The function def is part of the challenge so I can't remove self.
def removeDuplicates(self, head):
    temp, prev = head, None
    found_data = []

    while temp:
        if temp.data not in found_data:
            found_data.append(temp.data)
            if prev:
                prev.next = temp
            prev = temp
        else:
            prev.next = temp.next

        temp = temp.next

    return head