public class MidOfLinkedList {
    
    public static class Node {
        int data;
        Node next;

        Node(int x){
            data = x;
            next = null;
        }
    }

    public Node mid(Node head){
        // write your code here

        Node slow = head;

        if(head == null){
            return null;
        }

        Node fast = head.next;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
