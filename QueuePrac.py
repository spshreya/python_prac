class Queue:
    def __init__(self):
        self.queue=[]
    
    def pushh(self,data):
        self.queue.insert(0,data)
    
    def popp(self):
        if len(self.queue)<=0:
            return ('queue empty')
        else:
            return self.queue.pop()
    
    def frontt(self):
        if len(self.queue)<=0:
            return ('queue empty')
        else:
            return self.queue[-1]
            
    def rearr(self):
        if len(self.queue)<=0:
            return ('queue empty')
        else:
            return self.queue[0]
    
    def display(self):
        print(self.queue)       
            
def main():
    q=Queue()
    n=int(input())
    for i in range(n):
        data=input()
        q.pushh(data)
        
    q.display()
    print('popping an element')
    q.popp()
    q.display()
    
    print(q.rearr())
    print(q.frontt())
    
if __name__=='__main__':
    main()
