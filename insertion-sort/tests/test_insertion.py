import pytest
from ..insertion.insertion import InsertionSort


def test_insertion_sort_empty_list():
    input_list = []
    sorted_list = InsertionSort(input_list)
    assert sorted_list == []

def test_insertion_sort_already_sorted():
    input_list = [1, 2, 3, 4, 5]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted():
    input_list = [5, 4, 3, 2, 1]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [1, 2, 3, 4, 5]

def test_insertion_sort_duplicates():
    input_list = [4, 2, 3, 2, 1]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [1, 2, 2, 3, 4]

def test_insertion_sort_mixed_values():
    input_list = [9, 4, 2, 7, 5, 1, 8, 3, 6]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_insertion_sort_single_element():
    input_list = [42]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [42]

def test_insertion_sort_large_input():
    input_list = [5, 2, 1, 4, 8, 7, 6, 3]
    sorted_list = InsertionSort(input_list)
    assert sorted_list == [1, 2, 3, 4, 5, 6, 7, 8]

