import leetcode_16_odd_even_list.ListNode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

/**
 * Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 =
 * 807.
 * 
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]
 */

class P002_Add_Two_Number_Linked_Lists {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode resultList = new ListNode();
        ListNode root = resultList;
        int carryOver = 0;
        int sum = 0;
        while (l1 != null && l2 != null) {
            sum = (l1.val + l2.val + carryOver) % 10;
            carryOver = (l1.val + l2.val + carryOver) / 10;
            ListNode temp = new ListNode(sum);
            root.next = temp;
            root = root.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        while (l1 != null) {
            sum = (l1.val + carryOver) % 10;
            carryOver = (l1.val + carryOver) / 10;
            ListNode temp = new ListNode(sum);
            root.next = temp;
            root = root.next;
            l1 = l1.next;
        }

        while (l2 != null) {
            sum = (l2.val + carryOver) % 10;
            carryOver = (l2.val + carryOver) / 10;
            ListNode temp = new ListNode(sum);
            root.next = temp;
            root = root.next;
            l2 = l2.next;
        }

        if (carryOver > 0) {
            ListNode temp = new ListNode(carryOver);
            root.next = temp;
            root = root.next;
        }

        return resultList.next;
    }
}