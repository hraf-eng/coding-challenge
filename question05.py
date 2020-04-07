# 5. Remove duplicates on email thread:
# When different email clients are used on a same thread, the discussion get messy
# because old messages are included again and get duplicated. Given a email thread
# (represented by a singly unsorted linked list of messages), write a function that
# remove duplicated messages from it.
class ListCell:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        text = "Cell(" + self.value + ")"
        if self.next is None:
            return text
        else:
            return text + " -> \n" + str(self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        cell = ListCell(value)

        if self.head is None:
            self.head = cell
            self.tail = cell
        else:
            self.tail.next = cell
            self.tail = cell

    def find_value(self, value):
        node = self.head
        while node.next is not None:
            if node.value == value:
                return node
            node = node.next

    def remove_duplicates(self):
        node = self.head
        prev = None

        # Iterate on the list
        while node.next is not None:
            # Find first cell with the same value
            search = self.find_value(node.value)

            # If found something and it is a different cell
            if search is not None and search is not node:
                # If node is on the start change head
                if prev is None: 
                    self.head = node.next
                else: # Else link previous with next
                    prev.next = node.next
            prev = node
            node = node.next
        pass

    def __str__(self):
        return str(self.head)

my_list = LinkedList()
my_list.add("Message 1")
my_list.add("Message 2")
my_list.add("Message 1")
my_list.add("Message 3")
my_list.add("Message 4")
my_list.add("Message 2")
my_list.add("Message 5")
my_list.remove_duplicates()

print(my_list)
