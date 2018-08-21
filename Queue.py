class Queue(object):
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        '''
        向队尾插入项
        '''
        self.items.append(item)

    def size(self):
        return len(self.items)

    def dequeue(self):
        '''
        返回队首项，并从队列中删除该项
        '''
        if self.is_empty():
            return -1
        else:
            return self.items.pop(0)

    def is_empty(self):
        return self.size() == 0

    def show(self):
        if self.is_empty():
            print(-1)
        for i in range(self.size()):
            print(self.items[i],)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.size())
    q.show()
   