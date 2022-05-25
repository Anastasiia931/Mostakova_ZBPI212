# задача 1
# Напишите рекурсивную функцию fact, которая вычисляет факториал заданного числа x.

def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x - 1)

# задача 2
# Создайте функцию filter_even, которая принимает на вход список целых чисел, и фильтруя, возвращает
# список, содержащий только четные числа. Используйте filter для фильтрации и lambda

def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))

# задача 3
# Напишите функцию square ,которая принимает на вход список целых чисел и возвращает список с возведенными
# в квадрат элементами. Используйте map.

def square(li):
    return list(map(lambda x: x * x, li))

# задача 4
#Напишите функцию бинарного поиска bin_search, которая принимает на вход отсортированный список и элемент.
# Функция должна возвращать индекс искомого элемента в списке.

def bin_search(li, element):
    start = 0
    end = len(li)
    middle = 0
    while start <= end:
        middle = (start + end) // 2
        if element == li[middle]:
            return middle

        if element < li[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

# задача 5
# Напишите функцию is_palindrome определяющую,является ли строка палиндромом. Палиндромами являются текстовые
# строки, которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания,
# пробельные символы и цифры; регистр не имеет значения.

def is_palindrome(string):
    symbols = '.,!?:;()[]\{\}\'\"/\\- '
    for symb in string:
        if symb in symbols:
            string = string.replace(symb, '')
    string = string.replace(" ", "")
    string = string.lower()
    string = "".join(list(filter(lambda x: x.isalpha(), string)))
    left = 0
    right = len(string)-1
    count = 0
    while left != right:
        if (string[left] == string[right]):
            count += 1
        else:
            return "NO"
        left += 1
        right -= 1
    return "YES"

# задача 6
# Написать функцию calculate, которая принимает на вход текстовый файл содержащий строки следующего формата:
# Формат файла: арифметическая операция целое число #1 целое число #2\ Разделитель - 4 пробела
# Функция должна вернуть 1 строку. Строка содержит набор из чисел, разделенных запятой.
# После последнего числа запятая не ставится. Каждое число - результат операции:
# "результирующее целое число" = "целое число #1" применить "арифметическая операция" "целое число #2"

def calculate(path2file):
    result = []
    with open(path2file, encoding='utf-8') as file:
        for line in file.readlines():
            l = list(i.strip() for i in line.split())
            value1, value2 = int(l[1]), int(l[2])
            if l[0] == '+':
                result.append(str(value1 + value2))
            elif l[0] == '-':
                result.append(str(value1 - value2))
            elif l[0] == '*':
                result.append(str(value1 * value2))
            elif l[0] == '//':
                if value1 > 0 and value2 > 0:
                    result.append(str(value1 // value2))
                else:
                    print('Эта операция производится только с положительными числами')
            elif l[0] == '%':
                if value1 > 0 and value2 > 0:
                    result.append(str(value1 % value2))
                else:
                    print('Эта операция производится только с положительными числами')
            elif l[0] == '**':
                if value1 > 0 and value2 > 0:
                    result.append(str(value1 ** value2))
                else:
                    print('Эта операция производится только с положительными числами')
        return ','.join(result)

# задача 9
# Создайте класс с названием Student.

class Student(object):
    def __init__(self, name, surname, grades = [3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades
    def greeting(self):
        print('Hello, I am Student')
    def mean_grade(self):
        return sum(self.grades) / len(self.grades)
    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'
    def __add__(self, other):
        return self.name + ' is friends with ' + other.name
    def __str__(self):
        return self.fullname

# задача 10
# Определите класс исключений MyError, который принимает строковое сообщение msg в качестве параметра
# при инициализации и также имеет атрибут msg.

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg