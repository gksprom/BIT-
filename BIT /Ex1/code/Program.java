/**
 * The Program class contains methods to demonstrate basic Java functionality.
 * It includes a method to print a greeting message and a simple calculator method
 * that performs addition on random integers within a specified range.
 * The main method executes these tasks and measures the execution time of the calculator method.
 */
class Program 
{
    private static final int RANDOM_RANGE = 100000;

    // Task 1
    private static void hello_compiler() {
        System.out.println("Hello, Compiler World!");
    }

    // Task 2
    private static void calculator(int nb_loop) {
        for(int i = 0; i < nb_loop; i++) {
            int a = (int)(Math.random() * RANDOM_RANGE);
            int b = (int)(Math.random() * RANDOM_RANGE);
            System.out.println("a + b = " + (a + b));
        }
    }

    // Task 3
    static void bubbleSort(int arr[], int n) {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (swapped == false)
                break;
        }
    }

    // Task 4
    static private int divi(int a, int b) throws Exception {
       if (b == 0) {
            throw new Exception("division by 0");
       }
       return a / b;
    }

    // Function to print an array
    static void printArray(int arr[], int size){
        int i;
        for (i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Task 1");
        hello_compiler();

        System.out.println("Task 2");
        long startTime = System.nanoTime();
        calculator(100000);
        long endTime = System.nanoTime();
        System.out.println("Execution Time: " + (endTime - startTime) / 1e9 + " seconds");

        System.out.println("Task 3");
        int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
        bubbleSort(arr, arr.length);
        printArray(arr, arr.length);
        /* Will not work because the function don't take string array */
        //String arr2[] = { "Je", "suis", "en", "groupe", "avec", "un","grec", "il", "s'appel", "George" };
        //bubbleSort(arr2, arr2.length);
        //printArray(arr2, arr2.length);

        System.out.println("Task 4");
        int a = 10;
        int b = 3;
        System.out.println(divi(a, b));
    }
}
