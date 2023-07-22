import pytest
from Hash_Table.code.hashT import Hashtable

def test_set_and_get():
    hash_table = Hashtable()
    hash_table.set("name", "Husam")
    hash_table.set("age", 33)

    assert hash_table.get("name") == "John"
    assert hash_table.get("age") == 33


def test_collisions():
    hash_table = Hashtable()
    hash_table.set("Mohammad", "Al Sa'ed")
    hash_table.set("Malki", "Al Hudrob")

    assert hash_table.get("John") == "Doe"
    assert hash_table.get("Jake") == "Smith"


def test_has():
    hash_table = Hashtable()
    hash_table.set("name", "John")

    assert hash_table.has("name")
    assert not hash_table.has("age")


def test_keys():
    hash_table = Hashtable()
    hash_table.set("name", "John")
    hash_table.set("age", 30)

    keys = hash_table.keys()
    assert "name" in keys
    assert "age" in keys


def test_get_nonexistent_key():
    hash_table = Hashtable()
    with pytest.raises(KeyError):
        hash_table.get("nonexistent")


def test_set_overwrite_key():
    hash_table = Hashtable()
    hash_table.set("name", "John")
    hash_table.set("name", "Jane")

    assert hash_table.get("name") == "Jane"
