
class Node:

    def __init__(self,value=None,pointer=None):

        self.value=value
        self.pointer=pointer

class Stack:

    def __init__(self):
        self.head=None
        self.count=0

    def isEmpty(self):

        if self.count==0:
            return True

        else:
            return False

    def push(self,item):

        self.head=Node(item,self.head)
        self.count+=1

    def pop(self):
        if self.isEmpty():
            print("is empty")

        else:
            node=self.head
            self.head=node.pointer
            self.count-=1

            return node.value

    def peek(self):
        if self.isEmpty():
            print("is empty")

        else:
            return self.head.value

    def size(self):
        return self.count

    def _printList(self):
        node=self.head

        while node:
            print(node.value,end=' ')
            node=node.pointer
        print()


if __name__=="__main__":
    st=Stack()

    for i in range(10):
        st.push(i)

    print(st.size())
    print(st.peek())
    st.pop()
    st._printList()
