class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()  # Main stack for enqueue
        self.stack2 = Stack()  # Temporary stack for dequeue

    def enqueue(self, value):
        """
        Adds the given value to the pseudo queue by simulating an enqueue operation.
        
        Args:
        value: The value to be added to the pseudo queue.
        
        Returns:
        None
            
        (Big O) of the dequeue operation is O(1)
        """
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        """
        Removes and returns the value at the front of the pseudo queue, simulating a dequeue operation.
        
        Returns:
        The value at the front of the pseudo queue.
        
        Raises:
        IndexError: If the pseudo queue is empty.
            
        (Big O) of the enqueue operation is O(n)
        """
        
        if self.stack1.is_empty():
            raise IndexError("PseudoQueue is empty")
        return self.stack1.pop()
    
    
    
if __name__=="__main__":
    queue = PseudoQueue()

    
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)

    
    dequeued_value = queue.dequeue()
    print("Dequeued value:", dequeued_value)

   
    queue.enqueue(5)

    
    dequeued_value = queue.dequeue()
    print("Dequeued value:", dequeued_value)