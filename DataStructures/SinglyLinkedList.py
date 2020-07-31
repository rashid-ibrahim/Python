
class Node:
    def __init__(self, data=None, next_node=None):
        """
        Node class implemented in the linked list class below
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_node_at_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_node_at_place(self, value, place):
        if place == 0:
            self.insert_node_at_head(value)
        else:
            new_node = Node(value)
            count = 0
            temp = self.head
            while count < place:
                try:
                    temp = temp.next_node
                    count += 1
                except AttributeError:
                    break

            new_node.set_next(temp.next_node)
            temp.next_node = new_node

    def append_value(self):
        pass

    def insert_node_after_value(self, value, current_value, set_end=False):

        temp = self.head
        new_node = Node(value)
        while temp:
            if temp.get_data() == current_value:
                new_node.set_next(temp.next_node)
                temp.set_next(new_node)
                return True

        if set_end:
            # Todo: Implement append to end when that function is built.
            pass

        return False

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
            curr.next_node = prev
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
                prev.next_node.set_next(temp.next_node)
                return True
            else:
                prev = temp
                temp = temp.next_node
        return False

    def remove_duplicates(self):
        temp, prev = self.head, None
        found_data = []

        while temp:
            if temp.data not in found_data:
                found_data.append(temp.data)
                if prev:
                    prev.next_node = temp
                prev = temp

            else:
                prev.next_node = temp.next_node

            temp = temp.next_node

        return self.head

    def print_list(self):
        """
        Helper function to print out the contents of the list.
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next_node


def create_singly_linked_list(vals):
    linked_list = SinglyLinkedList([])
    while vals:
        val = vals.pop()
        linked_list.insert_node_at_head(val)

    return linked_list


if __name__ == '__main__':
    # Case 0
    test_vals = [1, 2, 2, 3, 3, 4]
    # Case 1
    # test_vals = [1, 1, 1, 1, 1, 1, 1]
    is_linked = create_singly_linked_list(test_vals)
    is_linked.print_list()
    print('Removing Duplicates')
    is_linked.remove_duplicates()
    is_linked.print_list()
    print('wait')
