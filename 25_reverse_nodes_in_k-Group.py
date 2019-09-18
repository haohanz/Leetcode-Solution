# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node):
            if not node or not node.next: return node, node
            head, tail = reverse(node.next)
            tail.next = node
            node.next = None
            return head, node

        cnt = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        prev = dummy
        while curr and cnt < k:
            cnt += 1
            curr = curr.next
        if curr:
            next = self.reverseKGroup(curr.next, k)
            curr.next = None
            head, tail = reverse(dummy.next)
            tail.next = next
        return head
