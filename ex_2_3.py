"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
import fractions

dict_of_alpha = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
                 13: 'd', 14: 'e', 15: 'f'}
number = 231434534
print(hex(number))


def get_10_on_16(num):
    process = ''
    while num > 0:
        process += dict_of_alpha.get((num % 16))
        num //= 16
    return process[::-1]


print(get_10_on_16(number))
"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""


def input_string():
    fraction = input()
    return fraction


def parser(string: str):
    string = string.replace(' ', '')
    a, b = string.split('/')
    return int(a), int(b)


print('Введи первую дробь формата: a/b')
first = parser(input_string())
print('Введи вторую дробь')
second = parser(input_string())


def multiple_fraction(first_fraction: tuple, second_fraction: tuple):
    return first_fraction[0] * second_fraction[0], second_fraction[1] * first_fraction[1]


def reduction(fraction: tuple):
    a = fraction[0]
    b = fraction[1]
    while a and b:
        if b > a:
            b %= a
        else:
            a %= b
    gcd = a or b
    num = int(fraction[0] / gcd), int(fraction[1] / gcd)
    if num[0] == num[1]:
        return 1
    else:
        return num


def addition(first_fraction: tuple, second_fraction: tuple):
    return first_fraction[0] * second_fraction[1] + second_fraction[0] * first_fraction[1], \
           first_fraction[1] * second_fraction[1]


def pars_of_fraction(fraction: tuple):
    if fraction.__sizeof__() == 28:
        return 1
    return f'{fraction[0]}/{fraction[1]}'


print(f'Умножение дробей: {(pars_of_fraction(reduction(multiple_fraction(first, second))))}')
print(f'Проверка: {fractions.Fraction(first[0], first[1]) * fractions.Fraction(second[0], second[1])}')
print(f'Сложение дробей: {(pars_of_fraction(reduction(addition(first, second))))}')
print(f'Проверка: {fractions.Fraction(first[0], first[1]) + fractions.Fraction(second[0], second[1])}')
