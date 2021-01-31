class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Display entire LinkedList
    def print_list(self):
        value = self.head
        collection = []
        while value is not None:
            collection.append(value.data)
            value = value.next
        print(collection)

    # Add value to start of LinkedList
    def prepend_value(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Add value to end of LinkedList
    def append_value(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Wrapper to remove function call parameters
    def getCount(self):
        return self.getCountRecursive(self.head)

    # Recursive function to summate all nodes
    def getCountRecursive(self, node):
        if (not node):
            return 0
        return 1 + self.getCountRecursive(node.next)

    # Non-recursive function
    def length(self):
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1
        return count


# Testing setup
list = LinkedList()
list.head = Node(9)
list.prepend_value(12)
list.append_value(7)
list.append_value(15)


print("Count is:", list.length())
list.print_list()
