public class KthNodeFromEnd {
    
    public static class Node {
        int data;
        Node next;

        Node(int x){
            data = x;
            next = null;
        }
    }

    public Node kthFromLast(Node head,int k){
        // write your code here

        Node a = head;
        Node b = head;

        for(int i=0 ; i<k ; i++){
            b = b.next;
        }

        while(b != null){
            a = a.next;
            b = b.next;
        }
        return a;
    }
}
