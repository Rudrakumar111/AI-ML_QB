class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, val):
        n = Node(val)
        if self.head == None :
            self.head = n
        else:
            n.next = self.head
            self.head = n
    
    def insert_middel(self,index,val):
        n = Node(val)
        if index < 1:
            return "give me index grater than one"
        if index == 1:
            n.next = self.head
            self.head = n
            return "Insert Successfully"
        if self.head == None:
            self.insert_first(val)
            return "Insert Successfully"
        else:
            self.r = self.head
            while(index != 2):
                index = index - 1
                self.head = self.head.next
            n.next = self.head.next
            self.head.next = n
            self.head = self.r
            return "Insert Successfully"

    def insert_end(self,val):
        n = Node(val)
        if self.head == None:
            self.insert_first(val)
        else:
            self.r = self.head
            while(self.r.next != None):
                self.r = self.r.next
            
            self.r.next = n

    def remove_ele(self,index):
        r = self.head
        if(index == 0 | index < 0):
            return "Please index greater then one"
        if(index > self.length()):
            return "You are try to remove element grater then length"
        if(index == 1):
            self.head = self.head.next
        else:
            c = 1
            while(c < index - 1):
                r = r.next
                c += 1
            n = r.next
            r.next = n.next

    def print_LL(self):
        self.r = self.head
        self.ele = []
        while(self.r != None):
            self.ele.append(self.r.val)
            self.r = self.r.next
        print(self.ele)
    
    def length(self):
        self.r = self.head
        length = 0
        while(self.r != None):
            self.r = self.r.next
            length = length + 1

        return length


obj = LinkedList()
obj.insert_first(20)
obj.insert_first(10)
obj.insert_end(30)
obj.insert_end(40)
obj.insert_end(50)
obj.insert_end(60)
obj.insert_middel(3,70)

print(obj.insert_middel(1,2))

obj.print_LL()
print(obj.remove_ele(9))

print(obj.length())

obj.print_LL()