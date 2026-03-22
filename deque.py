from collections import deque
import threading
import time
class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

def place_order(orders):
    for order in orders:
        pq.enqueue(order)
        time.sleep(0.5)
        
def serve_order():
    while pq.is_empty() is False:
        item = pq.dequeue()
        print(item)
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']
pq=Queue()

t1=threading.Thread(target=place_order,args=(orders,))
t2=threading.Thread(target=serve_order,args=())

t1.start()
t2.start()

t1.join()
t2.join()