public class Reverse {
    
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverse_Iterative(ListNode head) {
        // write your code here
        ListNode prev = null;
        ListNode cur = head;
        ListNode forw;

        while(cur != null){
            forw = cur.next;
            cur.next = prev;
            prev = cur;
            cur = forw;
        }
        return prev;
    }

    public ListNode reverse_Recursive(ListNode head) {

        if(head == null || head.next == null) {
            return head;
        }

        ListNode newHead = reverse_Recursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}
