# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Task1 import decorator1
from Task2 import decorator2
from Task3 import decorator3
from Task4 import decorator4


@decorator4
@decorator1
def even(input_list):
    """
    This function return even numbers in the given list
    :param input_list: List that we want to search for even number inside
    This function return the even numbers in the list
    """
    return list(filter(lambda x: x % 2 == 0, input_list))


@decorator4
@decorator1
def pascal(n):
    """
    This function print pascal triangle
    :param n: The number of pascal triangle rows
    This function return None
    """
    main_v = [1]
    added_v = [0]
    for _ in range(n):
        print(main_v)
        main_v = [left + right for left, right in zip(main_v + added_v, added_v + main_v)]


@decorator4
@decorator1
def factorial(n):
    """
    This function calculate factorial of integer n --> n!
    :param n: The value to calculate its factorial
    This function return the value of factorial for the given integer
    """
    assert n > 0, "Negative number passed to factorial function"
    if n < 2:
        return 1
    else:
        res = 1
        for x in range(1, n+1):
            res = res * x
        return res


@decorator4
@decorator1
def fib(n):
    """
    This function calculate Fibonacci series from 0 until n --> n!
    :param n: The value to calculate fibonacci until
    This function return a list contain fibonacci series from 1 to n
    """
    def fib_calc(p):
        assert p >= 0, "Negative number passed to factorial function"
        a, b = 1, 1
        while b < p:
            a, b = b, a + b
        return b
    return [fib_calc(x) for x in range(n)]


@decorator4
@decorator1
def test(n):
    """
    This function is for test purpose only
    :param n: input
    This function return 1/n to test division by zero exception
    """
    return 1/n


@decorator4
@decorator1
def q_solver(a, b, c):
    """
    This function solve a quadrant equation a*x^2 + b*x + c = 0
    :param a: x^2 factor
    :param b: x   factor
    :param c:     equation constant
    This function return the solution of QE if it exist in form of list
    """
    import cmath
    import math

    assert ((a != b) != c) != 0,  "You pass zero for all parameter"
    assert (a != b) != 0, "It is impossible expression"

    if a == 0:
        print('first degree equation, one solution')
        return c/b
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            print('QE with double solution')
            return [b / (2 * a)]
        elif delta > 0:
            print('QE with two solution')
            return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]
        else:
            print('QE with complex solution')
            return [(-b + cmath.sqrt(delta)) / (2 * a), (-b - cmath.sqrt(delta)) / (2 * a)]

@decorator4
@decorator1
def divider(n):
    """
    This function finds dividers of a given number.
    :param n: input number
    This function return list of input number dividers
    """
    return [list(filter(lambda x: n % x == 0, range(1, n)))]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pascal(3)
    test(1)
    factorial(5)
    pascal(3)
    test(0)
    factorial(5)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
