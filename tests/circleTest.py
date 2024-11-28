import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    '''
    Тестирование методов для круга на корректность работы
    '''
    
    '''
    Тестирование метода площади
    '''
    def test_area_zero(self):
        '''
        Тестирование со значением 0
        '''
        res = circle.area(0)
        self.assertEqual(res, 0)
        
    def test_area_positive(self):
        '''
        Тестирование с положительным числом
        '''
        res = circle.area(4)
        self.assertAlmostEqual(res, 50.26548245743669, places=5)  # Ожидаемое значение для радиуса 4

    def test_area_negative(self):
        '''
        Тестирование с отрицательным числом
        '''
        res = circle.area(-3)
        self.assertAlmostEqual(res, 28.274333882308138, places=5)  # Ожидаемое значение для радиуса -3 (возводится в квадрат)

    def test_area_string_input(self):
        '''
        Тестирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            circle.area("r")

    '''
    Тестирование метода периметра
    '''
    def test_perimeter_zero(self):
        '''
        Тестирование со значением 0
        '''
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_perimeter_positive(self):
        '''
        Тестирование с положительным числом
        '''
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876, places=5)  # Ожидаемое значение для радиуса 3

    def test_perimeter_negative(self):
        '''
        Тестирование с отрицательным числом
        '''
        res = circle.perimeter(-3)
        self.assertAlmostEqual(res, -18.84955592153876, places=5)  # Ожидаемое значение для радиуса -3

    def test_perimeter_string_input(self):
        '''
        Тестирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            circle.perimeter("r")


circle_tests = CircleTestCase