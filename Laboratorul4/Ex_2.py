class Queue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        return None

    def is_empty(self):
        return len(self.elements) == 0


def main():
    coada = Queue()
    coada.push(1)
    coada.push(2)
    coada.push(3)
    print(coada.pop())  # Va afișa 1
    print(coada.peek())  # Va afișa 2
    print(coada.pop())  # Va afișa 2
    print(coada.pop())  # Va afișa 3
    print(coada.pop())


main()
