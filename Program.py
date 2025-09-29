from random import randint
from typing import List
"""
This module contains functions to demonstrate basic operations such as printing a message,
performing calculations, and sorting a list using bubble sort.

Functions:
    hello_compiler(): Prints a greeting message to the compiler world.
    calculator(nb_loop: int) -> None: Performs addition of random integers and prints the results.
    bubbleSort(list: list) -> list: Sorts a list of integers using the bubble sort algorithm.
    div(a: int, b: int) -> int: Performs division of two integers and returns the result.

Constants:
    RANGE_RANDOM (int): The upper limit for generating random integers.

Execution:
    If the module is run as the main program, it performs the following tasks:
    1. Prints a greeting message.
    2. Performs a series of random additions and prints the execution time.
    3. Generates a list of random integers, sorts it using bubble sort, and prints the sorted list.
    4. Performs division of two random integers and prints the result.
"""
import time
RANGE_RANDOM: int = 100000

# Task 1
def hello_compiler():
    print("Hello, Compiler World!");

# Task 2
def calculator(nb_loop: int) -> None:
    for i in range(nb_loop):
        a: int = randint(1, RANGE_RANDOM)
        b: int = randint(1, RANGE_RANDOM)
        print(f"{a} + {b} = {a + b}")

# Task 3
def bubbleSort(list: list) -> list:
    n: int = len(list)
    for i in range(n):
        swapped: bool = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break

# Task 4
def div(a: int, b: int) -> int:
    if b == 0:
        Exception("Division by zero")
    return a / b

# Task 5
def matrix_mult(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res            

if '__main__' == __name__:
    print("Task 1")
    hello_compiler()

    print("Task 2")
    start_time: float = time.time()
    calculator(100000)
    end_time: float = time.time()
    print(f'Execution Time: {end_time - start_time:.6f} seconds')

    print("Task 3")
    list = [randint(1, RANGE_RANDOM) for i in range(1000)]
    bubbleSort(list)
    print("Sorted list is:")
    print(list)
    list2 = ["Je", "m'appel", "Pierre-Antoine", "Fournier.", "Je", "suis", "français"]; 
    bubbleSort(list2)
    print(list2)

    print("Task 4")
    a: int = randint(0, RANGE_RANDOM)
    b: int = randint(0, RANGE_RANDOM)
    print(div(a, b))

    print("Task 5")
    m1: List[List[int]] = [[randint(1, RANGE_RANDOM) for i in range(100)] for j in range(100)]
    m2: List[List[int]] = [[randint(1, RANGE_RANDOM) for i in range(100)] for j in range(100)]
    s: float = time.time()
    matrix_mult(m1, m2)
    e: float = time.time()
    print(f'Execution Time: {e - s:.6f} seconds')