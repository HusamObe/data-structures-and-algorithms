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
