"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
"""

# The Top Level folder on my computer is called GitHub
from GitHub.DataStructs import LinkedList


def setup_code(values1=None, values2=None):
    """
    This function is to setup all the boiler code as defined in the question
    :return:
    """
    values1 = [i for i in range(1, 15, 2)] if not values1 else values1
    values2 = [i for i in range(2, 16, 2)] if not values2 else values2

    linked1 = LinkedList.create_linked_list(values1)
    linked2 = LinkedList.create_linked_list(values2)

    return linked1, linked2


def main():
    # Setup two initial linked lists to use for the problem
    linked1, linked2 = setup_code()

    # Theoretically node1 and node2 variables are not needed but they make the code easier to read.
    node1, node2 = linked1.head, linked2.head
    merged_list = LinkedList.LinkedList([])

    while node1 and node2:
        if node1 and node1.get_data() < node2.get_data():
            merged_list.insert(node1.get_data())
            node1 = node1.get_next()
        elif node2 and node1.get_data() > node2.get_data():
            merged_list.insert(node2.get_data())
            node2 = node2.get_next()
        else:
            break

    return merged_list


if __name__ == '__main__':
    x = main()
    print('here')
