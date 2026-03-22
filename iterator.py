class Fibonacci:
    def __init__(self, limit):
        self.curr=0
        self.next=1
        self.n=1
        self.limit=limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n<self.limit:
            result=self.next+self.curr
            self.curr=self.next
            self.next=result
            self.n +=1
            return result
        else:
            raise Exception ("limit crossed")
        
    
fib_itr=iter(Fibonacci(10))
while True:
    try:
        print(next(fib_itr))
    except Exception as ex:
        print("exceptiopn caught",ex)
        break