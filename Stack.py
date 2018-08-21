class Stack(object):
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.items.pop()

    def clear(self):
        del self.items[:]

    def is_empty(self):
        return self.size() == 0

    def top(self):
        return self.items[self.size()-1]

    def show(self):
        if self.is_empty():
            print(-1)
        for i in range(self.size()):
            print(self.items[i],)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(3)
    print(s.size())
    s.pop()
    s.show()
    s.clear()
    s.show()

