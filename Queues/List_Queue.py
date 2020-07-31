
class Queue:

    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return not bool(self.items)


    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):

        if self.isEmpty():
            print("queue is empty")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):

        if self.isEmpty():
            print("queue is empty")

        else:
            return self.items[-1]

    def print_q(self):
        i=0

        while i<len(self.items):
            print(self.items[i], end=' ')
            i+=1






'''if __name__=="__main__":


    q=Queue()
    q.enqueue(10)
    q.dequeue()
    q.enqueue(30)
    print("is queue empty? {0}".format(q.isEmpty()))
    print("queue's waitintg list {0}".format(q.front()))
    print("q's size :{0}".format(q.size()))'''
