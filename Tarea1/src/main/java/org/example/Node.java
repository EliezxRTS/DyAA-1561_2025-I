package org.example;

public class Node {
    private Node upper;
    private Node center;
    private Node lower;
    private int value;

    public Node(Node upper, Node center, Node lower, int value) {
        this.upper = null;
        this.center = null;
        this.lower = null;
        this.value = value;
    }

    public Node getUpper() {
        return upper;
    }

    public void setUpper(Node upper) {
        this.upper = upper;
    }

    public Node getCenter() {
        return center;
    }

    public void setCenter(Node center) {
        this.center = center;
    }

    public Node getLower() {
        return lower;
    }

    public void setLower(Node lower) {
        this.lower = lower;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public void printValue() {
        System.out.println(this.getValue());
    }
}