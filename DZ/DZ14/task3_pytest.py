import pytest
from task3 import is_real_date


def test_year():
    assert is_real_date('31.02.2027') != True, 'Внимание! В феврале 28 или 29 дней'
    assert is_real_date('07.07.2027') != False, 'Внимание! Это реальная дата'
    assert is_real_date('31.06.2027')!= True, 'Внимание! В июне 30 дней'
    assert is_real_date('01.13.27') != True, 'Внимание! 13 месяцев в году не существует на нашей планете'
    assert is_real_date('24.07.10') != True, 'Внимание! Это реальная дата'
    assert is_real_date('12.07.2023') != True, 'Внимание! Это реальная дата'
    assert is_real_date('31.31.2000') != True, 'Внимание! 31 месяца в году не существует на нашей планете'


if __name__ == '__main__':
    pytest.main()