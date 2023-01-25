import pytest
from module.utils import *


def test_read_json():
    got = read_json("config.json")
    want = {'name': 'steve', 'lastname': 'jobs', 'age': '70', 'city': 'heaven'}
    assert isinstance(want, dict)
    assert got == want


def test_read_key_json():
    got = read_json("config.json", key="city")
    want = 'heaven'
    assert isinstance(want, str)
    assert got == want


def test_wrong_key_json():
    with pytest.raises(Exception) as e:
        read_json("config.json", key="not_a_key")

    assert "Wrong key" in str(e.value)


def test_wrong_jsonfile():
    with pytest.raises(Exception) as e:
        read_json("not_a_file.json")

    assert "file not found" in str(e.value)


def test_timer():
    start = timer()
    # do some operation
    l = list()
    for i in range(20):
        l.append(i)
    end = timer(start)


def test_class_items():
    print()
    start = timer()

    class Student:
        def __init__(self, name, age, grade):
            self.name: str = name
            self.age: int = age
            self.grade: str = grade

    student1 = Student("Issa", 25, "Master")
    end = timer(start)
    class_items(student1)


def test_list_intersec():
    lista = [1, 2, 3, 4]
    listb = [1, 4, 5, 6, 8, 7]
    listc = [10, 11, 12, 13]
    expected = [1, 4]
    assert expected == list_intersection(lista, listb)
    assert [] == list_intersection(lista, listc)


def test_list_diff():
    lista = [1, 2, 3, 4]
    listb = [1, 4, 5, 6, 8, 7]
    expected = [2, 3]
    assert expected == list_difference(lista, listb)
