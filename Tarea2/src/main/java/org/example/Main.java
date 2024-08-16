package org.example;

public class Main {
    public static void main(String[] args) {
        int[] array = {0,1,2,3,4,5,6,7,8,9}; //Asignacion T(n)=1
        for (int i=0; i < array.length; i++){ //Ciclo for T(n)=n        *Esto es para arreglos de tamaño n
            for (int j=0; j < array.length; j++){ //Ciclo for T(n)=n
                System.out.println("Pair: ("+ array[i] + "," + array[j] + ")"); //Impresion T(n)=1
            }
        }
        System.out.println("Total ordered pairs: " + array.length * array.length); //Impresion T(n)=1
    }
} //Total T(n) = 1 + n*(n*(1)) + 1 = n^2 + 2