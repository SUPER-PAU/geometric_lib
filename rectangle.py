from tests.rectangleTest import rect_tests
'''
импортирование инициализированного класса
RectangleTestCase для теста корректности работы методов
'''


def area(a, b): 
    '''
    метод принимает два числа: а (длину) и b (ширину). Находит и возвращает их произведение (площадь прямоугольника).
    пример работы:
    >>> area(5, 3)
    >>> 15
    '''

    return a * b 


def perimeter(a, b): 
    '''
    метод принимает два числа: а (длину) и b (ширину). Находит их удвоенную сумму (периметр прямоугольника).
    пример работы:
    >>> perimeter(5, 3)
    >>> 16
    '''

    return (a + b) * 2

