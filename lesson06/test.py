import pytest
from list_average import AverageGenerator, AverageComparator


def test_find_average_type_error():
    with pytest.raises(TypeError):
        AverageGenerator('Не строка')


def test_find_average_empty_error():
    with pytest.raises(ValueError):
        AverageGenerator()


def test_find_average_size_error():
    with pytest.raises(ValueError):
        AverageGenerator(1, 10, 100)


def test_find_average_checker_integration():
    avg1 = AverageGenerator(5, 1, 100)
    assert isinstance(avg1, AverageGenerator)


def test_find_average_end_to_end():
    avg1 = AverageGenerator(5, 1, 100)
    avg2 = AverageGenerator(5, 1, 100)
    assert AverageComparator.avg_compare(avg1.average, avg2.average)


@pytest.mark.parametrize("first_avg, second_avg, expected",
                         [(10, 5, 'Первое среднеарифметическое значение списка больше, чем второе.'),
                          (5, 10, 'Второе среднеарифметическое значение списка больше, чем первое.'),
                          (10, 10, 'Среднеарифметическое значение списков равно.')])
def test_is_prime(first_avg, second_avg, expected):
    assert AverageComparator.avg_compare(first_avg, second_avg) == expected