class Stack:
    def __init__(self):
        self.stack=[]
        
    def pushh(self,data):
        self.stack.append(data)
    
    def peekk(self):
        return self.stack[-1]
    
    def popp(self):
        if len(self.stack)<=0:
            return ('stack empty')
        else:
            return self.stack.pop()

def main():
    st = Stack()
    n=int(input())
    for i in range(n):
        data=input()
        st.pushh(data)
        
    print('topmost element is', st.peekk())
    print('removing from stack', st.popp())
    print('topmost element is',st.peekk())
    
if __name__=='__main__':
    main()
