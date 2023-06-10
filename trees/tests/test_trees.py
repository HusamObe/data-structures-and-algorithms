
from trees_datastructure.trees import BinarySearchTree


def test_instantiate_empty_tree():
    bst = BinarySearchTree()
    assert bst.root is None


def test_instantiate_tree_with_single_root():
    bst = BinarySearchTree()
    bst.add(5)
    assert bst.root.value == 5
    assert bst.root.left is None
    assert bst.root.right is None


def test_add_left_and_right_child():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    assert bst.root.value == 5
    assert bst.root.left.value == 3
    assert bst.root.right.value == 7


def test_pre_order_traversal():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(10)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    expected = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    assert bst.pre_order() == expected


def test_in_order_traversal():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(10)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    expected = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert bst.in_order() == expected


def test_post_order_traversal():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(10)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    expected = [1, 4, 7, 6, 3, 13, 14, 10, 8]
    assert bst.post_order() == expected


def test_contains_existing_value():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(10)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    assert bst.contains(6) is True


def test_contains_non_existing_value():
    bst = BinarySearchTree()
    bst.add(8)
    bst.add(3)
    bst.add(1)
    bst.add(6)
    bst.add(10)
    bst.add(14)
    bst.add(4)
    bst.add(7)
    bst.add(13)

    assert bst.contains(12) is False
