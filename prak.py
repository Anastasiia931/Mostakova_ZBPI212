# Мостакова А. ЗБ-ПИ21-2
from functools import reduce
def test_problem(func, test_data):
  """test helper"""
  for inputs, true_answer in test_data:
    if isinstance(inputs, tuple):
        answer = func(*inputs)
    else:
        answer = func(inputs)
    if answer != true_answer:
      print("wrong")
      return 0
  return 1

'''
  1
https://edabit.com/challenge/5XXXppAdfcGaootD9
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])
'''

def sum_odd_and_even(lst):
    return [sum(filter(lambda x:x%2==0,lst)),sum(filter(lambda x:x%2!=0,lst))]


def test_sum_odd_and_even(sum_odd_and_even_func):
    test_data = [
        ([1, 2, 3, 4, 5, 6], [12, 9]),
        ([-1, -2, -3, -4, -5, -6], [-12, -9]),
        ([0, 0], [0, 0]),
        ([], [0, 0])

    ]
    return test_problem(sum_odd_and_even_func, test_data)

print(test_sum_odd_and_even(sum_odd_and_even))



'''
  2
https://edabit.com/challenge/jpW2fAzfPtop8AYfW
Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
'''

def to_dict(lst):
    return list(map(lambda x:{x:ord(x)},lst))


def test_to_dict(to_dict_func):
    test_data = [
        (["a", "b", "c"], [{"a": 97}, {"b": 98}, {"c": 99}]),
        (["!", ".", "?"], [{"!": 33}, {".": 46}, {"?": 63}]),
        (["^"], [{"^": 94}]),
        ([" "], [{" ": 32}]),
        ([], [])

    ]
    return test_problem(to_dict_func, test_data)

print(test_to_dict(to_dict))


'''
   3
https://www.codewars.com/kata/5a3a95c2e1ce0efe2c0001b0/python
The written representation of a number (with 4 or more digits) can be split into three parts in various different ways. 
For example, the written number 1234 can be split as [1 | 2 | 34] or [1 | 23 | 4] or [12 | 3 | 4].

Given a written number, find the highest possible product from splitting it into three parts and multiplying 
those parts together. For example:

product of [1 | 2 | 34] = 1 * 2 * 34 = 68
product of [1 | 23 | 4] = 1 * 23 * 4 = 92
product of [12 | 3 | 4] = 12 * 3 * 4 = 144
So maximumProductOfParts(1234) = 144
'''


def maximum_product_of_parts(n):
    number = str(n)
    max_product = 0
    for p1 in range(1, len(number) - 1):
        for p2 in range(p1 + 1, len(number)):
            parts = (int(i) for i in (number[:p1], number[p1:p2], number[p2:]))
            product = reduce(lambda x, y: x * y, parts)
            if product > max_product:
                max_product = product

    return max_product


def test_maximum_product_of_parts(maximum_product_of_parts_func):
    test_data = [
        (1234, 144),
        (4321, 252),
        (4224, 352)

    ]
    return test_problem(maximum_product_of_parts_func, test_data)

print(test_maximum_product_of_parts(maximum_product_of_parts))



