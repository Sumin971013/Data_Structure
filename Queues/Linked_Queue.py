
class Node:
    def __init__(self,value=None,pointer=None):
        self.value=value
        self.pointer=pointer


class Linked_queue:

    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def isEmpty(self):
        return not bool(self.head)

    def enqueue(self,value):
        node=Node(value) # 삽입 노드 생성

        if self.isEmpty(): # 비어있는 경우
            self.head=node
            self.tail=node

        else: # 기존에 있을 때는 테일의 포인터만 변경
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

    def size(self):
        return self.count

    def peek(self):

        if self.isEmpty():
            print("queue is empty")

        else:
            return self.head.value


    def print_queue(self):

        node=self.head

        if self.isEmpty():
            print("queue is empty")

        while node:
            print(node.value,"-> ", end='  ')
            node=node.pointer
        print()





if __name__=="__main__":

    lq=Linked_queue()
    lq.enqueue(10)
    lq.enqueue(50)
    lq.enqueue(30)
    lq.enqueue(40)

    lq.dequeue()
    lq.print_queue()
    print(lq.peek())







