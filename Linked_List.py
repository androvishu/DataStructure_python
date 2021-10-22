import IPython.core.magic


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Liked List is Empty!")
            return
        i = self.head
        llist = ''
        while i:
            llist += str(i.data) + '-->'
            i = i.next
        print(llist + "None")

    def insert_at_begning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= ll.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= ll.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begning(data)

        count = 0
        i = self.head
        while i:
            if count == index - 1:
                node = Node(data, i.next)
                i.next = node
                break
        i = i.next
        count += 1

    def insert_after_value(self, data_after, data_to_insert):
        count = data_after
        itr = self.head
        while itr:
            if count == itr.data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            else:
                print(data_after, "is not present in this Linked List!")
                break

            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data.capitalize())

    def find_index(self, data):
        count = 0
        itr = self.head
        while itr:
            if data == itr.data:
                return count
            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        index = ll.find_index(data)
        self.remove_at(index)
        print('Remove', str(data) + " Element", "at", str(index) + "'th index")


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begning(12)
    ll.insert_at_begning(84)

    ll.insert_at_end(78)
    ll.insert_at_end(1)
    ll.insert_at(1, 9793)
    ll.insert_after_value(84, "Vishal")

    ll.print_list()
    ll.remove_by_value(9793)

