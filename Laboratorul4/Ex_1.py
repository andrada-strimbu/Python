class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        return None

    def is_empty(self):
        return len(self.elements) == 0


def main():
    stiva=Stack()
    stiva.push(1)
    stiva.push(2)
    stiva.push(3)
    print(stiva.pop())
    print(stiva.peek())
    print(stiva.pop())
    print(stiva.pop())
    print(stiva.pop())

main()