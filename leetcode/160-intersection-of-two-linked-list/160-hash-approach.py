# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Hash Solution, time complexity O(m+n), space complexity O(m)
        # where m and n are the length of headA and headB respevtively.


        # create a hashmap to store
        hashtable = {}

        # two pointer, one for each linked list
        probeA = headA
        probeB = headB

        # traverse A and puts the memory address as key input the hash
        while probeA:
            hashtable[id(probeA)] = probeA.val        
            probeA = probeA.next

        # traverse b, check memory address of node in b is in the key space of the hash

        while probeB:
            if id(probeB) in hashtable.keys():
                return probeB

            probeB = probeB.next

        return None
