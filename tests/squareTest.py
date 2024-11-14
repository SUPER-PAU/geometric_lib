import unittest
import square

class SquareTestCase(unittest.TestCase):
    '''
    Тестирование методов для квадрата на корректность работы
    '''
    
    '''
    Тестирование метода площади
    '''
    def test_area_zero(self):
        '''
        Тестирование со значением 0
        '''
        res = square.area(0)
        self.assertEqual(res, 0)
        
    def test_area_positive(self):
        '''
        Тестирование с положительным числом
        '''
        res = square.area(5)
        self.assertEqual(res, 25)  # Ожидаемое значение: 5 * 5 = 25

    def test_area_negative(self):
        '''
        Тестирование с отрицательным числом
        '''
        res = square.area(-4)
        self.assertEqual(res, 16)  # Ожидаемое значение: (-4) * (-4) = 16
    
    def test_area_string_input(self):
        '''
        Тестирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            square.area("a")

    '''
    Тестирование метода периметра
    '''
    def test_perimeter_zero(self):
        '''
        Тестирование со значением 0
        '''
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_perimeter_positive(self):
        '''
        Тестирование с положительным числом
        '''
        res = square.perimeter(5)
        self.assertEqual(res, 20)  # Ожидаемое значение: 5 * 4 = 20

    def test_perimeter_negative(self):
        '''
        Тестирование с отрицательным числом
        '''
        res = square.perimeter(-4)
        self.assertEqual(res, -16)  # Ожидаемое значение: -4 * 4 = -16
    
    def test_perimeter_string_input(self):
        '''
        Тестирование с вводом строки
        '''
        res = square.perimeter("A")
        self.assertEqual(res, "AAAA")


square_tests = SquareTestCase