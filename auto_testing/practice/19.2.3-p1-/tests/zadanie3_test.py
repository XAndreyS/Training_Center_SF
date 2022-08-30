import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_multiply_calculate_corrrectly(self):
        """Проверяем умножение целых положительных чисел,получаем целое положительное число, позитивный тест"""
        assert self.calc.multiply(self, 22, 22) == 484

    def test_division_correctly(self):
        """Проверяем деление целых положительных чисел, большее делим на меньшее и получаем целое положительное число,
        позитивный тест"""
        assert self.calc.division(self, 21, 3) == 7

    def test_subtraction_correctly(self):
        """ПРоверяем вычитание целых положительных чисел, из большего меньшее и получаем целое положительное число,
         позитивный тест"""
        assert self.calc.subtraction(self, 20, 10) == 10

    def test_adding_correctly(self):
        """Проверяем сложение целых  положительных чисел, позитивный тест"""
        assert self.calc.adding(self, 100, 100) == 200

