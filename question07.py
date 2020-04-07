# 7. Linked List Intersection:
# If two requests on the queue have linked lists that intersect (like the example below),
# previous service could be improved to process only the difference between them.
# Write a method that receives two singly linked lists and return the intersecting node
# of the two lists (if exists). Note that the intersection is defined by reference, not value.
# (No need to change previous answer).
class ListCell:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Cell(" + self.value + ")"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        self.add_cell(ListCell(value))

    def add_cell(self, cell):
        if self.head is None:
            self.head = cell
            self.tail = cell
        else:
            self.tail.next = cell
            self.tail = cell

    def find_cell(self, cell):
        node = self.head
        while node.next is not None:
            if node == cell:
                return node
            node = node.next

    def find_intersection(self, other_list):
        node = self.head
        while node.next is not None:
            if other_list.find_cell(node):
                return node
            node = node.next
        return None

    def __str__(self):
        return str(self.head)

cell_j = ListCell("J")

list1 = LinkedList()
list1.add("C")
list1.add("A")
list1.add("E")
list1.add("H")
list1.add_cell(cell_j)
list1.add("B")
list1.add("A")

list2 = LinkedList()
list2.add("D")
list2.add("F")
list2.add_cell(cell_j)

print("Intersection: ", list1.find_intersection(list2))