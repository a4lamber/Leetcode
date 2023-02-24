# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # set up a hashmap for storing unique values in the linked list as keys
        value_hash = {}

        # create a dummy header node
        dummy_header = ListNode(None,None)
        dummy_header.next = head

        # set a `curr` pointer to the start of the linkd list
        curr = dummy_header
        
        # 链表中remove method如下
        while curr.next: 
            if curr.next.val not in value_hash.keys():
                # 还没碰到这个元素，放入hash
                value_hash[curr.next.val] = 1
                # moves forward both pointer by one
                curr = curr.next
            else:
                # 说明碰到过了, remove this node
                curr.next = curr.next.next
        

        return head





