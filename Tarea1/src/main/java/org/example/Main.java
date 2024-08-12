package org.example;

import java.util.List;

public class Main {
    public static void main(String[] args) {

        // Creamos un nuevo grafo 'graph' y su nodo cabecera 'head'
        TernaryGraph graph = new TernaryGraph();
        Node head = new Node(null, null, null, 20);
        graph.setHead(head);

        // Insercion de los nodos
        graph.insertNode(head, 23, "upper");       // Nivel 1: head -> upper
        graph.insertNode(head, 19, "center");       // Nivel 1: head -> center
        graph.insertNode(head.getUpper(), 57, "center"); // Nivel 2: head -> upper -> center
        graph.insertNode(head.getCenter(),67,"lower"); // Nivel 2: head -> center -> lower
        graph.insertNode(head.getCenter().getLower(), 99, "center"); // Nivel 3: head -> center -> lower -> center

        // Imprimir la ruta desde la cabecera al nodo con valor 57 siguiendo una lista de posiciones correctas
        System.out.println("Path from head to 57 following the known route:");
        List<String> pathTo57 = List.of("upper", "center");
        graph.printPathFromHead(pathTo57);

        // Imprimir la ruta desde la cabecera al nodo con valor 99 siguiendo una lista de posiciones correctas
        System.out.println("Path from head to 99 following the known route:");
        List<String> pathTo99 = List.of("center", "lower", "center");
        graph.printPathFromHead(pathTo99);

        // Imprimir la ruta desde la cabecera al nodo con valor 99 siguiendo una lista de posiciones incorrectas
        System.out.println("Path from head to 99 following an arbitrary route:");
        List<String> pathTo99Wrong = List.of("center", "lower", "upper");
        graph.printPathFromHead(pathTo99Wrong);
    }
}