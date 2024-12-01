import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_subtraction(): # вычитание
       assert calculate.subtract(10, 5) == 5
       assert calculate.subtract(0, 0) == 0
       assert calculate.subtract(-5, -5) == 0
       assert calculate.subtract(-5, 5) == -10
       assert calculate.subtract(5, -5) == 10

def test_multiplication(): # умножение
       assert calculate.multiply(3, 4) == 12
       assert calculate.multiply(0, 5) == 0
       assert calculate.multiply(-3, -4) == 12
       assert calculate.multiply(-3, 4) == -12
       assert calculate.multiply(3, -4) == -12

def test_division_by_zero(): # деление на ноль
       try:
           calculate.divide(5, 0)
           assert False, "Expected ValueError"
       except ValueError:
           pass
'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо, как минимум, добавить тесты для следующих операций:
1. Вычитание
2. Умножение
Но будет круто, если ты сможешь придумать и добавить дополнительные тесты
'''
