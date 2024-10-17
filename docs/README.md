# GEOMETRIC_LIB

## Содержание
1) О проекте
2) Структура проекта
3) Формулы
4) Описание Функций и пример работы
5) История изменений


## О проекте
Проект написан на языке python. Содержит 4 файла .py, в которых описаны функции для нахождения площади и периметра геометрических фигур:
* Круг
* Квадрат
* Треугольник
* Прямоугольник

## Структура проекта

    ./geometric_lib
    ├── circle.py
    ├── square.py
    ├── triangle.py
    ├── rectangle.py
    └── docs
        └── README.md

## Формулы

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Описание Функций и пример работы

### файл circle.py:
------
#### Метод нахождения площади
```python
def area(r):
    # На вход поступает число r (радиус). Метод возвращает площадь круга (pi * r^2).
    return math.pi * r * r
```
пример работы:
```cmd
>>> area(4)
50.26548245743669
```
#### Метод нахождения периметра
```python
def perimeter(r):
    # На вход поступает число r (радиус). Метод возвращает периметр круга (2 * pi * r)
    return 2 * math.pi * r
```
пример работы:
```cmd
>>> perimeter(3)
18.84955659215387
```

------
### файл square.py:
------
функция нахождения площади
```python
def area(a):
    # Метод принимает число а (сторону квадрата). Возвращает квадрат числа а (площадь квадрата).
    return a * a

```
пример работы:
```cmd
>>> area(5)
25
```

#### Метод нахождения периметра
```python
def perimeter(a):
    # Метод принимает число а (сторону квадрата). Возвращает а * 4 (периметр квадрата).
    return 4 * a
```
пример работы:
```cmd
>>> perimeter(5)
20
```
------
### файл rectangle.py:
------
функция нахождения площади
```python
def area(a, b): 
    # метод принимает два числа: а (длину) и b (ширину). Находит и возвращает их произведение (площадь прямоугольника).
    return a * b 

```
пример работы:
```cmd
>>> area(5, 3)
15
```

#### Метод нахождения периметра
```python
def perimeter(a, b): 
    # метод принимает два числа: а (длину) и b (ширину). Находит их удвоенную сумму (периметр прямоугольника).
    return (a + b) * 2
```
пример работы:
```cmd
>>> perimeter(5, 3)
16
```

------
### файл triangle.py:
------
функция нахождения площади
```python
def area(a, h):
    # Метод получает на вход 2 числа: a и h (основание и высота треугольника). Метод возвращает площадь треугольника (a * h) / 2.
    return a * h / 2 
```
пример работы:
```cmd
>>> area(5, 6)
15
```

#### Метод нахождения периметра
```python
def perimeter(a, b, c):
    # Метод получает на вход 3 числа: a, b, c (все 3 стороны треугольника). Метод возвращает периметр треугольника (сумму всех сторон).
    return a + b + c 
```
пример работы:
```cmd
>>> perimeter(5, 3, 4)
12
```

## История изменений
```cmd
* commit 628d570a32dde8ec7d935a15294f30c3d6fe6580 (HEAD ->  new_features_466109, origin/new_features_466109)
| Author: SUPER-PAU <superpauks@gmail.com>
| Date:   Thu Oct 17 19:56:34 2024 +0300
| 
|     создал новый файл triangle.py и исправил функцию в файле rectangle.py
| 
* commit 8ce9539e0291c4217a8444ebb868923a62dd0694
| Author: SUPER-PAU <superpauks@gmail.com>
| Date:   Thu Oct 17 19:55:31 2024 +0300
| 
|     создал новый файл rectangle.py
|   
| * commit ced1943493eb1807b57e4b0c9f1f736169a64153 (new_br)
|/  Author: SUPER-PAU <superpauks@gmail.com>
|   Date:   Fri Oct 4 10:19:17 2024 +0300
|   
|       changed req.py
| 
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
| 
|     L-03: Docs added
| 
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300
  
      L-03: Circle and square added
```