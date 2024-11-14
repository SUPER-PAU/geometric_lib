import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    '''
    тестирование методов прямоугольника на корректность работы
    '''
    
    '''
    тестирование методов площади
    '''
    def test_area_zero_mul(self):
        '''
        тестрирование со значением 0
        '''
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_square_mul(self):
        '''
        тестрирование на квадрат
        '''
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative_nums(self):
        '''
        тестрирование с отрицательными значениями
        '''
        res = rectangle.area(10, -10)
        self.assertEqual(res, -100)
    
    def test_area_default_case(self):
        '''
        тестрирование обычного случая
        '''
        res = rectangle.area(6, 5)
        self.assertEqual(res, 30)

    def test_area_string_input(self):
        '''
        тестрирование с вводом строки
        '''
        res = rectangle.area("a", 8)
        self.assertEqual(res, "aaaaaaaa")
    
    def test_area_both_string_input(self):
        '''
        тестрирование с вводом 2-ух строк
        '''
        with self.assertRaises(TypeError):
            rectangle.area("a", "b")
    
    '''
    тестирование методов периметра
    '''
    def test_perimeter_zero_add(self):
        '''
        тестрирование со значением 0
        '''
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
        
    def test_perimeter_equal(self):
        '''
        тестрирование на квадрат
        '''
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_negative_nums(self):
        '''
        тестрирование с отрицательными значениями
        '''
        res = rectangle.perimeter(10, -5)
        self.assertEqual(res, 10)
    
    def test_perimeter_default_case(self):
        '''
        тестрирование обычного случая
        '''
        res = rectangle.perimeter(6, 5)
        self.assertEqual(res, 22)

    def test_perimeter_string_input(self):
        '''
        тестрирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            res = rectangle.perimeter("A", 8)
    
    def test_perimeter_both_string_input(self):
        '''
        тестрирование с вводом 2-ух строк
        '''
        res = rectangle.perimeter("a", "B")
        self.assertEqual(res, "aBaB")


rect_tests = RectangleTestCase
