import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    '''
    тестирование методов треугольника на корректность работы
    '''
    
    '''
    тестирование метода площади
    '''
    def test_area_zero_mul(self):
        '''
        тестирование со значением 0
        '''
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_square_mul(self):
        '''
        тестирование с равными значениями основания и высоты
        '''
        res = triangle.area(10, 10)
        self.assertEqual(res, 50)

    def test_area_negative_nums(self):
        '''
        тестирование с отрицательными значениями
        '''
        res = triangle.area(10, -10)
        self.assertEqual(res, -50)

    def test_area_default_case(self):
        '''
        тестирование обычного случая
        '''
        res = triangle.area(6, 5)
        self.assertEqual(res, 15)

    def test_area_string_input(self):
        '''
        тестирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            triangle.area("a", 8)
    
    def test_area_both_string_input(self):
        '''
        тестирование с вводом 2-ух строк
        '''
        with self.assertRaises(TypeError):
            triangle.area("a", "b")
    
    '''
    тестирование метода периметра
    '''
    def test_perimeter_zero_add(self):
        '''
        тестирование со значением 0
        '''
        res = triangle.perimeter(10, 0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_equal_sides(self):
        '''
        тестирование для равностороннего треугольника
        '''
        res = triangle.perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_negative_nums(self):
        '''
        тестирование с отрицательными значениями
        '''
        res = triangle.perimeter(10, -5, 5)
        self.assertEqual(res, 10)

    def test_perimeter_default_case(self):
        '''
        тестирование обычного случая
        '''
        res = triangle.perimeter(6, 5, 4)
        self.assertEqual(res, 15)

    def test_perimeter_string_input(self):
        '''
        тестирование с вводом строки
        '''
        with self.assertRaises(TypeError):
            triangle.perimeter("A", 8, 6)
    
    def test_perimeter_both_string_input(self):
        '''
        тестирование с вводом 2-ух строк
        '''
        with self.assertRaises(TypeError):
            triangle.perimeter("a", "B", 3)


triangle_tests = TriangleTestCase
