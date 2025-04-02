class ListNode:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
# 707. 设计链表
class MyLinkedList(object):

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size: return
        if index < 0: index = 0
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val, cur.next)
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

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
    # 206. 反转链表
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = head
        pre = None
        while dummy_head:
            tmp = dummy_head.next
            dummy_head.next = pre
            pre = dummy_head
            dummy_head = tmp
        return pre
    # 19. 删除链表的倒数第N个元素
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0,head)
        fast = dummy_head
        slow = dummy_head
        while n and fast:
            fast = fast.next
            n -=1
        fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_head.next




sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

r = sol.removeNthFromEnd(head,1)
while r:
    print(r.val)
    r = r.next
