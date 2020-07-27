class Node:

    def __init__(self, data=None, next_node=None, previous=None):
        """
        Node class implemented in the linked list class below
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

    def insert_node_at_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_node_at_tail(self, data):
        temp = self.head
        new_node = Node(data)

        while True:
            next_node = temp.next_node
            if new_node:
                temp = next_node
            else:
                break

        new_node.set_previous(temp)
        temp.next_node = new_node

    def insert_node_at_place(self, value, place):
        if place == 0:
            self.insert_node_at_head(value)
        else:
            new_node = Node(value)
            count = 0
            temp = self.head
            while count < place:
                # This try handles if a higher place than the length of the list is given
                try:
                    temp = temp.next_node
                    count += 1
                except AttributeError:
                    break

            next_node = temp.next_node
            if next_node:
                next_node.set_previous(new_node)

            new_node.set_next(next_node)
            new_node.set_previous(temp)
            temp.next_node = new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def reverse(self):
        prev, next_el = None, None
        curr = self.head

        while curr:
            next_el = curr.next_node
            curr.set_next(prev)
            curr.set_previous(next_el)
            prev, curr = curr, next_el

        self.head = prev

    def search(self, value):
        """
        Ultimately a search function depends on what you want it to do.
        This particular one will check if a given value is in the list.
        :param value: Value to search for. Depending on what is stored in the list, this data type will change.
        :return: Bool if the value is found or not. This can be made to return other things depending on the search type
        """
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next_node

        return False

    def update(self, old_value, new_value):
        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return True
            temp = temp.next_node

        return False

    def delete(self, value):
        """
        Removes a specific value, if found, from the linked list and updates the node references
        :param value: Value to delete. The data type depends on what is stored in the list.
        :return: Returns none
        """
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                next_node = temp.next_node
                prev.set_next(next_node)
                next_node.set_previous(prev)
            else:
                prev = temp
                temp = temp.next_node
        return None

    def print_list(self):
        """
        Helper function to print out the contents of the list.
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next_node


def create_doubly_linked_list(vals):
    linked_list = DoublyLinkedList([])
    while vals:
        val = vals.pop()
        linked_list.insert_node_at_head(val)

    return linked_list


if __name__ == '__main__':
    test_vals = [1, 2, 3, 4, 5]
    is_linked = create_doubly_linked_list(test_vals)
    is_linked.print_list()
    print('Reversing')
    is_linked.reverse()
    is_linked.print_list()
    print('wait')