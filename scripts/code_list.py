class ListNode:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
class Solution(object):
    # 203. 移除链表元素
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
val = 6
res = sol.removeElements(head, val)
while res:
    print(res.val)
    res = res.next
