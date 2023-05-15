class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result
    
    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    
    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("List is empty. Cannot insert before.")
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception("Value not found. Cannot insert before.")
    
    
    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("List is empty. Cannot insert after.")
        current = self.head
        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception("Value not found. Cannot insert after.")



if __name__ == "__main__":
    
    my_list = LinkedList()


    my_list.insert('d')
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')


    print(my_list.includes('b'))  
    print(my_list.includes('d'))  
    print(my_list.includes('f')) 

    print(my_list.to_string())
    
    
    # Append
    my_list.append(5)
    print(my_list.to_string())  # Output: { a } -> { b } -> { c } -> { d } -> { 5 } -> NULL

    # Insert Before
    my_list.insert_before('b', 'x')
    print(my_list.to_string())  # Output: { a } -> { x } -> { b } -> { c } -> { d } -> { 5 } -> NULL

    # Insert After
    my_list.insert_after('c', 'y')
    print(my_list.to_string())  # Output: { a } -> { x } -> { b } -> { c } -> { y } -> { d } -> { 5 } -> NULL
