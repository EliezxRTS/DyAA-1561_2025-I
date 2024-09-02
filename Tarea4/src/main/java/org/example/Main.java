package org.example;

public class Main {

    public static int fibonacci(int fibNumber) {
        if (fibNumber == 0) {
            return fibNumber;
        } else if (fibNumber == 1) {
            return fibNumber;
        } else {
            return fibonacci(fibNumber - 1) + fibonacci(fibNumber - 2);
        }
    }

    public static void main(String[] args) {
        int serie = fibonacci(8);
        System.out.println("Resultado: " + serie);
    }
}