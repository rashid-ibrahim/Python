
class Node:
    def __init__(self, data=None, next_node=None):
        """
        Node class implmented in the linked list class below
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self):
        # TODO: implement search
        pass

    def delete(self):
        # TODO: implement delete
        pass


def create_linked_list(vals):
    linked_list = LinkedList([])
    while vals:
        val = vals.pop()
        linked_list.insert(val)

    return linked_list


if __name__ == '__main__':
    test_vals = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    is_linked = create_linked_list(test_vals)
    print('wait 2')
