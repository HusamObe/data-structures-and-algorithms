import pytest
from linked_list.linked_list import LinkedList

def test_instantiate_empty_linked_list():
    my_list = LinkedList()
    actual = my_list.head
    expected = None
    assert actual == expected

def test_insert_into_linked_list():
    my_list = LinkedList()
    my_list.insert('a')
    actual = my_list.head.value
    expected = 'a'
    assert actual == expected

def test_head_points_to_first_node():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    actual = my_list.head.value
    expected = 'b'
    assert actual == expected

def test_insert_multiple_nodes():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    actual = (my_list.head.value, my_list.head.next.value, my_list.head.next.next.value)
    expected = ('c', 'b', 'a')
    assert actual == expected

def test_search_existing_value():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    actual = my_list.includes('b')
    expected = True
    assert actual == expected

def test_search_non_existing_value():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    actual = my_list.includes('f')
    expected = False
    assert actual == expected

def test_get_all_values():
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    actual = my_list.to_string()
    expected = "{ c } -> { b } -> { a } -> NULL"
    assert actual == expected


def test_append_multiple_nodes():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    actual = my_list.to_string()
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_before_existing_value():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_before('b', 'x')
    actual = my_list.to_string()
    expected = "{ a } -> { x } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_before_head():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_before('a', 'x')
    actual = my_list.to_string()
    expected = "{ x } -> { a } -> { b } -> { c } -> NULL"
    assert actual == expected

def test_insert_after_existing_value():
    my_list = LinkedList()
    my_list.append('a')
    my_list.append('b')
    my_list.append('c')
    my_list.insert_after('b', 'x')
    actual = my_list.to_string()
    expected = "{ a } -> { b } -> { x } -> { c } -> NULL"
    assert actual == expected
    
    
    
def test_kthFromEnd_greater_than_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)

    with pytest.raises(Exception) as e_info:
        ll.kthFromEnd(5)
    assert str(e_info.value) == "k is larger than the length of the linked list."

def test_kthFromEnd_same_length():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(3)
    expected = 1
    assert actual == expected

def test_kthFromEnd_not_positive_integer():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)

    with pytest.raises(ValueError) as e_info:
        ll.kthFromEnd(-2)
    assert str(e_info.value) == "k should be a non-negative integer."

def test_kthFromEnd_single_node():
    ll = LinkedList()
    ll.append(5)

    actual = ll.kthFromEnd(0)
    expected = 5
    assert actual == expected

def test_kthFromEnd_middle_of_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)

    actual = ll.kthFromEnd(2)
    expected = 3
    assert actual == expected
    
def test_merge_linked_lists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    
    list2 = LinkedList()
    list2.append(4)
    list2.append(5)
    list2.append(6)

    merged_list = LinkedList.merge_linked_lists(list1, list2)


    assert merged_list.to_string() == "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> { 3 } -> { 6 } -> NULL"


def test_merge_linked_lists_with_empty_list():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = LinkedList()

    merged_list = LinkedList.merge_linked_lists(list1, list2)

    assert merged_list.to_string() == "{ 1 } -> { 2 } -> { 3 } -> NULL"
    
    
def test_merge_linked_lists_with_two_empty_lists():
    list1 = LinkedList()
    list2 = LinkedList()

    merged_list = LinkedList.merge_linked_lists(list1, list2)

    assert merged_list.to_string() == "NULL"

def test_merge_linked_lists_with_duplicates():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)

    merged_list = LinkedList.merge_linked_lists(list1, list2)

    assert merged_list.to_string() == "{ 1 } -> { 1 } -> { 2 } -> { 2 } -> { 3 } -> { 3 } -> NULL"

