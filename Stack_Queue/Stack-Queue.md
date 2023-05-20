# Stack:
* A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It means that the last element added to the stack is the first one to be removed. Think of it like a stack of plates, where you can only add or remove plates from the top. The top of the stack represents the most recently added element, while the bottom represents the least recently added element.

# Node:
The Node class represents a single node in the linked list. It has two properties:

* `value`: Stores the value of the node.
* `next`: Points to the next node in the linked list.

# Stack Implementation:

The `Stack` class is implemented using a linked list, where the top of the stack is represented by the first node in the linked list.

**push(value):**
* The `push` method adds a new element to the top of the stack. It takes a `value` parameter representing the value of the new element. The steps involved are:

<ol>
<li>Create a new "Node" object with the given value.</li>
<li>If the stack is empty (i.e., self.top is None), assign the new node to self.top.</li>
<li>If the stack is not empty, set the next attribute of the new node to the current top node, and update self.top to the new node.</li>
</ol>

**pop():**
* The pop method removes and returns the element from the top of the stack. It does the following:

<ol>
<li>Check if the stack is empty. If so, raise an exception since there are no elements to remove.</li>
<li>Store the value of the current top node in a variable called value.</li>
<li>Update self.top to the next node in the stack, effectively removing the current top node.</li>
<li>Return the value that was stored in step 2.</li>
</ol>

**peek():**
* The `peek` method returns the value of the element at the top of the stack without removing it. The steps are:
<ol>
<li>Check if the stack is empty. If so, raise an exception since there are no elements to peek.</li>
<li>Return the value of the top node in the stack.</li>
</ol>

**is_empty():**
* The `is_empty` method checks whether the stack is empty or not. It returns `True` if the stack is empty (i.e., `self.top` is None), and `False` otherwise.

---
# Queue:
A queue is a linear data structure that follows the `First-In-First-Out` `(FIFO)` principle. It works like a line of people waiting for a service, where the first person who joins the line is the first one to be served.

# Queue Implementation:

**enqueue(value):**
* The `enqueue` method adds a new element to the rear of the queue. It takes a `value` parameter representing the value of the new element. 
The steps involved are:
<ol>
<li>Create a new Node object with the given value.
<li>If the queue is empty, assign the new node to both self.front and self.rear.
<li>If the queue is not empty, set the next attribute of the current rear node to the new node, and update self.rear to the new node.
</ol>

**dequeue():**
* The `dequeue` method removes and returns the element from the front of the queue. It does the following:
<ol>
<li>Check if the queue is empty. If so, raise an exception since there are no elements to remove.
<li>Store the value of the current front node in a variable called value.
<li>Update self.front to the next node in the queue, effectively removing the current front node.
<li>If the queue becomes empty after dequeueing, update self.rear to None.
<li>Return the value that was stored in step 2.
</ol>


**peek():**
* The `peek` method returns the value of the element at the front of the queue without removing it. The steps are:
<ol>
<li>Check if the queue is empty. If so, raise an exception since there are no elements to peek.
<li>Return the value of the front node in the queue.
</ol>

**is_empty():**
The `is_empty` method checks whether the queue is empty or not. It returns `True` if the queue is empty (i.e., `self.front` is `None`), and `False` otherwise.
