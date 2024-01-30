#Тестовый модуль
from bot import first
from main.first import nums_sum
def test_sum1():
    assert nums_sum('23 3') == 26