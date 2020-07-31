class Node:

    def __init__(self,value=None,pointer=None):

        self.value=value
        self.pointer=pointer



class LinkedQueue:

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def isEmpty(self):
        return  not bool(self.head)

    def enqueue(self,item):
        node=Node(item)

        if not self.head: #큐가 비어있는 경우 삽입하는 것
            self.head=node
            self.tail=node

        else:
            if self.tail:
                self.tail.pointer=node

            self.tail=node
        self.count+=1


    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")

        else:
            value=self.head.value
            self.head=self.head.pointer
            self.count-=1

        return value

    def peek(self):
        if self.isEmpty():
            print("queue is empty")

        else:
            return self.head.value


    def size(self):
        return self.count

    def print_all(self):
        node=self.head

        while node:
            print(node.value,end=' ')
            node=node.pointer

        print()


if __name__=="__main__":
    q=LinkedQueue()
    q.enqueue(10)
    q.enqueue(40)
    q.dequeue()
    print("is q empty? {}".format(q.isEmpty()))

    q.print_all()