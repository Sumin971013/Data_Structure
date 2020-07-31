
from Queues import List_Queue

class Deque(List_Queue.Queue):
    def enqueue_back(self,item):
        self.items.append(item)

    def dequeue_front(self):
        if self.items:
            return self.items.pop(0)

        else:
            print("queue is empty")



if __name__=="__main__":
    dq=Deque()
    print("is dequqe empty {0}".format(dq.isEmpty()))
    print("adding 0~9 into deque")
    for i in range(10):
        dq.enqueue(i)

    print("size of dq:{0}".format(dq.size()))
    print("peek : {}".format(dq.front()))

