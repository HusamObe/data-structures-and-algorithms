class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception("Stack is empty!!")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if not self.top:
            raise Exception("Stack is empty!!")
        return self.top.value

    def is_empty(self):
        return not bool(self.top)
    
def validate_brackets(string):
    stack = Stack()
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in bracket_pairs.keys():
            stack.push(char)
        elif char in bracket_pairs.values():
            if stack.is_empty() or bracket_pairs[stack.pop()] != char:
                return False

    return stack.is_empty()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            raise Exception("Queue is empty!!")
        value = self.front.value
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            raise Exception("Queue is empty!!")
        return self.front.value

    def is_empty(self):
        return not bool(self.front)



if __name__=='__main__':
    # Stack testing
    stack = Stack()
    stack.push("www.facebook.com")
    stack.push("www.facebook.com/home")
    stack.push("www.facebook.com/about")

    print(stack.peek())  

    print(stack.pop())  
    print(stack.pop())  
    print(stack.is_empty())  
    print(stack.pop())  
    print(stack.is_empty()) 
    
    # Queue Testing 
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.peek())  

    print(queue.dequeue())  
    print(queue.dequeue())  
    print(queue.is_empty()) 
    print(queue.dequeue())  
    print(queue.is_empty())  
    
    
    print("################# BRACKETS BALANCE CHECKER #########################")
    print(validate_brackets("{}"))  
    print(validate_brackets("{}(){}"))  
    print(validate_brackets("()[[Extra Characters]]"))  
    print(validate_brackets("(){}[[]]"))  
    print(validate_brackets("{}{Code}[Fellows](())"))  
    print(validate_brackets("[({}]"))  
    print(validate_brackets("(]("))  
    print(validate_brackets("{(})")) 