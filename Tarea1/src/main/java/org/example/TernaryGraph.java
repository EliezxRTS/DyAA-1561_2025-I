package org.example;

import java.util.List;
public class TernaryGraph {
    private Node head;

    public TernaryGraph() {
        this.head = null;
    }

    public void setHead(Node head) {
        this.head = head;
    }

    public Node getHead() {
        return head;
    }

    //Metodo para insertar los nodos en posiciones especificas: 'upper', 'center', 'lower'
    public void insertNode(Node parent, int value, String position) {
        Node newNode = new Node(null, null, null, value);

        if (parent == null) {
            System.out.println("Parent node is null. Cannot insert.");
            return;
        }

        switch (position.toLowerCase()) {
            case "upper":
                if (parent.getUpper() == null) {
                    parent.setUpper(newNode);
                    System.out.println("Inserted " + value + " at upper of " + parent.getValue());
                } else {
                    System.out.println("Upper is already occupied at node " + parent.getValue() + ". Cannot insert " + value + ".");
                }
                break;
            case "center":
                if (parent.getCenter() == null) {
                    parent.setCenter(newNode);
                    System.out.println("Inserted " + value + " at center of " + parent.getValue());
                } else {
                    System.out.println("Center is already occupied at node " + parent.getValue() + ". Cannot insert " + value + ".");
                }
                break;
            case "lower":
                if (parent.getLower() == null) {
                    parent.setLower(newNode);
                    System.out.println("Inserted " + value + " at lower of " + parent.getValue());
                } else {
                    System.out.println("Lower is already occupied at node " + parent.getValue() + ". Cannot insert " + value + ".");
                }
                break;
            default:
                System.out.println("Invalid position: " + position + ". Use 'upper', 'center', or 'lower'.");
                break;
        }
    }

    // Método para imprimir la ruta desde la cabecera siguiendo una lista de posiciones
    public void printPathFromHead(List<String> path) {

        Node currentNode = head;
        System.out.print("Path from head: " + currentNode.getValue() + " -> ");

        for (String position : path) {
            switch (position.toLowerCase()) {
                case "upper":
                    currentNode = currentNode.getUpper();
                    break;
                case "center":
                    currentNode = currentNode.getCenter();
                    break;
                case "lower":
                    currentNode = currentNode.getLower();
                    break;
                default:
                    System.out.println("Invalid position: " + position + ". Use 'upper', 'center', or 'lower' only.");
                    return;
            }
            if (currentNode == null) {
                System.out.println("Reached a null node. Path incomplete.");
                return;
            }
            System.out.print(currentNode.getValue() + " -> ");
        }
        System.out.println("End of path");
    }
}
