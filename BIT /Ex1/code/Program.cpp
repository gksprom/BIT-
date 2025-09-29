/**
 * @file Program.cpp
 * @brief A simple C++ program demonstrating basic tasks and performance measurement.
 * 
 * This program includes two tasks:
 * 1. Printing a hello message to the console.
 * 2. Performing a series of random multiplications and measuring the execution time.
 * 4. A function that performs division and handles division by zero.
 * 
 * The program uses the <iostream> library for console output and the <chrono> library for measuring execution time.
 * 
 */

#include <iostream>
#include <chrono>
#include <cstdlib>


const int random_range = 100000;

// Task 1
void hello_compiler() {
    std::cout << "Hello, Compiler World!" << std::endl;
}

// Task 2
void calculator(int nb_loop) {
    for (int i = 0; i < nb_loop; i++) {
        int a = rand() % random_range;
        int b = rand() % random_range;
        std::cout << a * b << std::endl;
    } 
}

// Task 4
int divi(int a, int b) {
    if (a == 0) {
        std::cerr << "Division by zero" << std::endl;
        return -1;
    }
    return b / a;
}

int main() {
    
    // Task 1
    std::cout << "Task 1" << std::endl;
    hello_compiler();
    
    //Task 2
    std::cout << "Task 2" << std::endl;
    auto start = std::chrono::high_resolution_clock::now();
    calculator(100000);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Execution Time: " << elapsed.count() << " seconds" << std::endl;

    // Task 4
    int a = rand() % random_range;
    int b = rand() % random_range;
    std::cout << divi(a, b) << std::endl;

    return 0;
}
