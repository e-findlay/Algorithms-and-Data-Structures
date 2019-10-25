class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after

#####################################################

def good_expression(expression):
    #create queue and stack
    q = Queue()
    s = Stack()
    #counter for pair of brackets
    count0 = 0
    #counter for whether brackets are nested
    count1 = 0
    #store character before open bracket in x
    x = []
    #store characters between 2 brackets in z
    z = ''
    #store whether a '+' was between 2 brackets in a
    a = []
    Next = False
  
    for i in range(0, len(expression)):
        #if last element was a closed bracket, check if this element or element before last open bracket was asterisk 
        if Next:
            Next = False
            if x[-1] != '*' and expression[i] != '*':
                return False
            else:
                x.pop()
        
        #if inside a pair of brackets, add character to queue
        if count1 > 0:
            q.enqueue(expression[i])
        #increment both counters if inside an open bracket
        if expression[i] == '(':
            count0 += 1
            
            #if first element is not a bracket, add last element in stack to x
            if i > 0:
                x.append(s.pop())
            #if first element is a bracket, add ''0' to x
            else:
                x.append('0')
            #empty the queue into z
            if count1 > 0:
                while q.isEmpty() == False:
                    z += str(q.dequeue())
                #if a '+' was found in the queue, append '+' to list a
                if z.find('+') != -1:
                    a.append('+')
                    z = ''
                #if no '+' was found, append '0' to list a
                else:
                    a.append('0')
                    z = ''
            count1 += 1
        #add character to stack
        s.push(expression[i])
        #if closed bracket, decrement second counter to show outside a pair of brackets
        if expression[i] == ')':
            count1 -= 1
            #change Next to True to check next element in expression to see if asterisk
            if i != len(expression)-1:
                Next = True
            #if no more items in expression, check if element before last open bracket was asterisk
            else:
                if x[-1] != '*':
                    return False
            #empty queue into z if inside brackets
            while q.isEmpty() == False:
                z += str(q.dequeue())
            #if a '+' was in the queue, append '+' to a else append '0' to a
            if z.find('+') != -1:
                a.append('+')
                z = ''
            else:
                a.append('0')
                z = ''
    #check there was a '+' between each pair of brackets
    for k in range(0, len(a)):
        if a[k] != '+' and a[len(a)-k-1] != '+':
            if len(a) == 0:
                return True
            return False
    return True
            

def testq3():
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4")
    assert not good_expression("((1+2))*3+4")
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)") 
    print ("all tests passed")
    

