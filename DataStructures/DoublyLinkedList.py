class Node:

    def __init__(self, data=None, next_node=None, previous=None):
        """
        Node class implmented in the linked list class below
        """
        self.data = data
        self.next_node = next_node
        self.previous = previous

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_prev):
        self.previous = new_prev


class DoublyLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.previous = tail

    def insert_node_at_head(self):
        pass

    def insert_node(self):
        pass

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def reverse(self):
        pass

    def search(self):
        pass

    def delete(self):
        pass

    def print_list(self):
        pass
