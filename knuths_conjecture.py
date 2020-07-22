from decimal import *

class Node:
    def __init__(self,data,op,parent):
        self.parent = parent           # storing the parent of the node 
        self.data = data               # storing the data of the node
        self.operation = op            # storing the operation that created this node
        
def calculateFactorial():
    factorial = [1]
    for i in range(1,20001):
        factorial.append(factorial[i-1]*i)
    return factorial

def Display_Sequence(ans):
    answer = []
    while ans != None:
        #answer.append(ans.operation+' --> '+str(ans.data))
        answer.append(ans.operation)
        ans = ans.parent
    
    i = len(answer)-1
    while i >= 0:
        print(answer[i],end='-->')
        i -= 1
    print(n)

def Knuths_Conjecture(n,factorial):
    node = Node(4,'4',None)
    queue = [node]    
    
    node_hash_map = {4:1}

    while True:
        node = queue.pop(0)
            
        if node.data == n:
            ans = node
            break
        val = node.data
        
        if val < 10000:
            fact = factorial[val]
            try:
                temp = node_hash_map[fact]
            except KeyError:
                node_hash_map[fact] = 1
                queue.append(Node(fact,'Factorial',node))                 # storing the factorial of current value
            
        val = int(Decimal(val).sqrt())  
        try:
            temp = node_hash_map[val]
        except KeyError:
            node_hash_map[val] = 1
            queue.append(Node(val,'Square Root-->Floor',node))        # storing the floor value of square root
    
    Display_Sequence(ans)
        

if __name__ == '__main__':
    factorial = calculateFactorial()
    n = int(input('Enter the value of n: '))
    Knuths_Conjecture(n,factorial)
