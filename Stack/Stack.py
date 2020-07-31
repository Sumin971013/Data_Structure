class Stack():

    def __init__(self):
        self.items=[]

    def isEmpty(self):

        return not bool(self.items)

    def push(self,item):

        self.items.append(item)


    def pop(self):

        value=self.items.pop()

        if value is not None:
            return  value

        else:
            print("it is empty")

    def size(self):
        return len(self.items)

    def peek(self):

        value=self.items[-1]



'''if __name__=="__main__":
    st=Stack()
    print(st.size())

    st.push(10)
    print(st.size())'''

