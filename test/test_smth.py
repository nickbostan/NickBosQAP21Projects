import random

import pytest


@pytest.fixture(scope="session")
def lst():
    lst_temp = []
    for i in range(10):
        lst_temp.append(random.randint(0, 100))

    return lst_temp


def test_1(lst):
    assert 10 == 10


def test_2(lst):
    assert lst[-1] == 0
