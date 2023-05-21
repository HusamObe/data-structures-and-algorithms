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
    
    def kthFromEnd(self, k):
        if k < 0:
            raise ValueError("k should be a non-negative integer.") # raise error for non-positive values

        if self.head is None:
            raise Exception("The linked list is empty.") # raise error for empty linked list 

        slow_pointer = self.head
        fast_pointer = self.head

        # Move the fast pointer k nodes ahead of slow pointer
        for _ in range(k):
            if fast_pointer.next is None:
                raise Exception("k is larger than the length of the linked list.") # raise error if k is bigger than the linked list size
            fast_pointer = fast_pointer.next

        # Move both pointers until the fast pointer reaches the end
        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        return slow_pointer.value       
    
            
    def merge_linked_lists(list1, list2):
        merged_list = LinkedList()
        current1 = list1.head  
        current2 = list2.head  

        while current1 is not None and current2 is not None:
            merged_list.append(current1.value)
            current1 = current1.next

            merged_list.append(current2.value)
            current2 = current2.next

        #for thee remaining nodes from list1 just incase
        while current1 is not None:
            merged_list.append(current1.value)
            current1 = current1.next

        #for the remaining nodes from list2 just in case
        while current2 is not None:
            merged_list.append(current2.value)
            current2 = current2.next

        return merged_list
        
        



if __name__ == "__main__":
    
    # my_list = LinkedList()


    # my_list.insert('d')
    # my_list.insert('c')
    # my_list.insert('b')
    # my_list.insert('a')


    # print(my_list.includes('b'))  
    # print(my_list.includes('d'))  
    # print(my_list.includes('f')) 

    # print(my_list.to_string())
    
    
    # # Append
    # my_list.append(5)
    # print(my_list.to_string())  # Output: { a } -> { b } -> { c } -> { d } -> { 5 } -> NULL

    # # Insert Before
    # my_list.insert_before('b', 'x')
    # print(my_list.to_string())  # Output: { a } -> { x } -> { b } -> { c } -> { d } -> { 5 } -> NULL

    # # Insert After
    # my_list.insert_after('c', 'y')
    # print(my_list.to_string())  # Output: { a } -> { x } -> { b } -> { c } -> { y } -> { d } -> { 5 } -> NULL
    
    # print("oxoxoxox",my_list.kthFromEnd(4))
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)

    list2 = LinkedList()
    list2.append(5)
    list2.append(6)
    list2.append(7)
    list2.append(8)

    
    merged_list = LinkedList.merge_linked_lists(list1, list2)

    
    print(merged_list.to_string())