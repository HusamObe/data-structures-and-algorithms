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