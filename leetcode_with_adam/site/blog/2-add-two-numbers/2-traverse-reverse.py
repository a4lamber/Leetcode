# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # intuition:
        # 1. traverse the linked list and put its value inside a str, O(n);
        # 2. reverse the string and cast it to int, O(n);
        # 3. do the addition and determine whether we gonna 升一个digit or not;
        # 4.1 if 升级，多加一个node
        # 4.2 如果不升级，直接将string, 一个一个塞进node就行
        
        # Step 1: 
        l1_str = ""
        l2_str = ""

        probe1, probe2 = l1, l2

        while probe1:
            l1_str += str(probe1.val)
            probe1 = probe1.next

        while probe2:
            l2_str += str(probe2.val)
            probe2 = probe2.next

        # step 2 reverse the string
        def helper(s):

            s = list(s)

            left,right = 0,len(s) -1
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            
            return "".join(s)

        l1_str = helper(l1_str)        
        l2_str = helper(l2_str)

        resultString = str(int(l1_str) + int(l2_str))

        # assign it
        head = None

        for char in resultString:
            head = ListNode(int(char),head)
        
        return head


