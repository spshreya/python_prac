class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class ll:
    
    def __init__(self):
        self.head=None
        self.last_node=None
        
    def append(self,data):
        
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head  
        else:
            self.last_node.next= Node(data)
            self.last_node=self.last_node.next
    
    def disply(self):
        current = self.head
        while current is not None:
            print(current.data,end=' ')
            current= current.next
            

def main():
    al=ll()
    n=int(input('enter no of nodes: '))
    for i in range(n):
        data=int(input('data:'))
        al.append(data)
        
    al.disply()
    
if __name__=='__main__':
    main()
