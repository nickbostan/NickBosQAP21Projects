import math
import random
import unittest

import pytest

"1.Первое задание на проверку простого числа и его тестирование"


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def test_small1():  # Тест малых простых чисел
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(7)
    assert is_prime(5)


def test_large1():  # Тест больших простых чисел
    assert is_prime(97)
    assert not is_prime(100)
    assert is_prime(101)


def test_small_composite1():  # Тест малых составных чисел
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)


def test_large_composite1():  # Тест больших составных чисел
    assert not is_prime(99)
    assert not is_prime(24)
    assert not is_prime(100000000000000)


def test_negative1():  # Тест негативных значений
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(1)


# Это я подсмотрел в интернете черех блок unittest , потому что pycharm мне подсветил сразу именно этот вариант


class test_prime(unittest.TestCase):
    def test_small(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(5))

    def test_large(self):
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))
        self.assertTrue(is_prime(101))

    def test_small_composite(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_large_composite(self):
        self.assertFalse(is_prime(99))
        self.assertFalse(is_prime(100000000000000000000))
        self.assertFalse(is_prime(24))

    def test_negative(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(1))


if __name__ == "__main__":
    unittest.main()


"2.Второе задание на нахождение и вывод индекса массы тела с последующим тестированием плюс параметризация"


def imt(w, h):
    try:
        if w <= 0 or h <= 0:
            raise ValueError("Значения должны бть положительными")
        h = h / 100
        index = w / (h**2)

        if index < 16:
            return "выраженный дефицит"
        elif 16 <= index < 18.5:
            return "дефицит"
        elif 18.5 <= index < 25:
            return "норма"
        elif 25 <= index < 30:
            return "избыточность"
        elif 30 <= index < 35:
            return "ожирение 1 степени"
        elif 35 <= index < 40:
            return "ожирение 2 степени"
        elif index > 40:
            return "ожирение 3 степени"

    except ValueError:
        return "Error"


@pytest.fixture  # Генерация тестовых данных
def random_test_data():
    test_data = []
    for i in range(5):
        weight = random.uniform(20, 120)
        height = random.uniform(20, 220)
        test_data.append((weight, height))
    return test_data


def test_random_data(random_test_data):  # Тест со случайными данными
    expected_cat = [
        "выраженный дефицит",
        "дефицит",
        "норма",
        "избыточность",
        "ожирение 1 степени",
        "ожирение 2 степени",
        "ожирение 3 степени",
    ]
    for weight, height in random_test_data:
        result = imt(weight, height)
        assert isinstance(result, str)
        assert result in expected_cat


@pytest.mark.parametrize(
    "weight, height, expected",
    [
        (45, 170, "выраженный дефицит"),
        (50, 170, "дефицит"),
        (65, 170, "норма"),
        (80, 170, "избыточность"),
        (95, 170, "ожирение 1 степени"),
        (110, 170, "ожирение 2 степени"),
        (140, 170, "ожирение 3 степени"),
    ],
)
def test_norm_val(
    weight, height, expected
):  # Проверка нормальных значений в каждой категории
    assert imt(weight, height) == expected


def test_extr_high_val():  # Проверка больших значений
    assert imt(200, 150) == "ожирение 3 степени"
    assert imt(150, 110) == "ожирение 3 степени"


@pytest.mark.parametrize(
    "weight, height, expected",
    [
        (40, 160, "выраженный дефицит"),
        (41, 160, "дефицит"),
        (47, 160, "дефицит"),
        (48, 160, "норма"),
        (63, 160, "норма"),
        (65, 160, "избыточность"),
        (76, 160, "избыточность"),
        (77, 160, "ожирение 1 степени"),
        (89, 160, "ожирение 1 степени"),
        (90, 160, "ожирение 2 степени"),
        (102, 160, "ожирение 2 степени"),
        (103, 160, "ожирение 3 степени"),
    ],
)
def test_boarder_val(weight, height, expected):  # Проверка по граничным значениям
    assert imt(weight, height) == expected


@pytest.mark.parametrize(
    "weight, height, expected",
    [
        (-50, 160, "Error"),
        (89, -160, "Error"),
        (0, 160, "Error"),
        (89, 0, "Error"),
        (-89, -160, "Error"),
    ],
)
def test_wrong_val(weight, height, expected):  # Негативные проверки
    assert imt(weight, height) == expected
