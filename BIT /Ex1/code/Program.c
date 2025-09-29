#include <stdlib.h>
#include <err.h>
#include <stdio.h>
#include <time.h>

const int RANDOM_RANGE = 1000;

// Task 4

/**
 * @brief Make a division and handle errors
 * @param a and int, b an int
 * @return error if a = 0 or b / a
 */
int divi(int a, int b) {
    if (a == 0) {
        errx(EXIT_FAILURE, "Division by zero");
    }
    return b / a;
}

// Task 5
/**
 * @brief Multiply two matrices of arbitrary size
 * @param mat1 First matrix
 * @param mat2 Second matrix
 * @param r1 Number of rows in mat1
 * @param c1 Number of columns in mat1
 * @param r2 Number of rows in mat2
 * @param c2 Number of columns in mat2
 * @return Resultant matrix or NULL if multiplication is not possible
 */
int** matrix_mult(int** m1, int** m2, size_t r1, size_t c1, size_t r2, size_t c2) {
    int** res = (int**)(calloc(c2, sizeof(int*)));
    // can be optimize
    for (size_t i = 0; i < c1; i++) {
        res[i] = calloc(r2, sizeof(int));
    }
    //
    for (size_t i = 0; i < r1; i++) {
        for (size_t j = 0; j < c2; j++) {
            for (size_t k = 0; k < r2; k++) {
                res[i][j] = res[i][j] + m1[i][k] * m2[k][j];
            }
        }
    }
    return res;
}

int main() {
    printf("Task 4\n");
    int a = rand() % RANDOM_RANGE;
    int b = rand() % RANDOM_RANGE;
    printf("%d\n", divi(a, b));
    

    printf("Task 5\n");
    int** m1 = malloc(100 * sizeof(int*));
    for (size_t i = 0; i < 100; i++) {
        m1[i] = malloc(sizeof(int) * 100);
        for (size_t j = 0; j < 100; j++) {
            m1[i][j] = rand() % 10;
        }
    }
    int** m2 = malloc(sizeof(int) * 100);
    for (size_t i = 0; i < 100; i++) {
        m2[i] = malloc(sizeof(int) * 100);
        for (size_t j = 0; j < 100; j++) {
            m2[i][j] = rand() % 10;
        }
    }
    clock_t start = clock();
    int** res = matrix_mult(m1, m2, 100, 100, 100 ,100);
    clock_t end = clock();
    printf("Time: %f\n", (double)(end - start) / CLOCKS_PER_SEC);
    for(size_t i = 0; i < 10; i++) {
        for(size_t j = 0; j < 10; j++) {
            printf("%d |", res[i][j]);
        }
        printf("\n");
    }

    return EXIT_SUCCESS;
}   
