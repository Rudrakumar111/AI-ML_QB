class Queue:
    def __init__(self,l):
        self.q = []
        self.l = l

    def enqueue(self,e):
        if(self.isFull()):
            return "Queue is Full"
        self.q.append(e)
        return "add Successfully"

    def dequeue(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        return self.q.pop(0) 
    
    def first(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        return self.q[0]
    
    def last(self):
        if(self.isEmpty()):
            return "Queue is Empty"
        
        return self.q[-1]

    
    def isEmpty(self):
        return len(self.q) == 0 
            

    def isFull(self):
        return (len(self.q) == self.l)
    
    def __str__(self):
        return str(self.q)

    def length(self):
        return len(self.q)
    
q = Queue(10)
print(q)
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(6)

print(q)
print(q.first())
print(q.dequeue())

print(q)

print(q.last())
print(q.dequeue())
print(q)