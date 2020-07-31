
class Queue:

    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]


    def _transfer(self):

        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self,item):
       return self.in_stack.append(item)

    def dequeue(self):

        if len(self.out_stack) ==0:
            self._transfer()

        if self.out_stack:
            return self.out_stack.pop()

        else:
            print("Queue is empty")

    def size(self):
        return len(self.out_stack)+len(self.in_stack)


    def peek(self):
        if not self.out_stack:
            self._transfer()

        if self.out_stack:
            return self.out_stack[-1]

        else:
            print("empty")


    def isEmpty(self):
        return not bool(self.out_stack) | bool(self.in_stack)



'''if __name__=="__main__":
    q=Queue()
    q.enqueue(30)
    q.enqueue(50)
    q.dequeue()


    print("q is empty? {0}".format(q.isEmpty()))
    print("q size: {}".format(q.size()))
    print("next waiting {0}".format(q.peek()))'''

