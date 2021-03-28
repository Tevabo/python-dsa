test1 = '(())()'  # should pass
test2 = '())()()'  # should fail
test3 = '(((())))'  # should pass


# Stack implementation where end of the list is the top
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items - 1)]

    def size(self):
        return len(self.items)


def check_parentheses(arr):
    stack = Stack()
    for char in arr:
        if char == '(':
            stack.push(char)
        elif stack.isEmpty():
            return False
        else:
            stack.pop()
    return stack.isEmpty()


print(check_parentheses(test2))
