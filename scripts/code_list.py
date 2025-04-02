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
    # 链表相交
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA, lengthB = 0, 0
        dummy_A = headA
        dummy_B = headB
        while dummy_A:
            lengthA += 1
            dummy_A = dummy_A.next
        while dummy_B:
            lengthB += 1
            dummy_B = dummy_B.next
        if lengthA < lengthB:
            headA, headB = headB, headA
            lengthA, lengthB = lengthB, lengthA
        curA = headA
        n = lengthA - lengthB
        while n and curA:
            curA = curA.next
            n -= 1
        curB = headB
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
    # 142.环形链表二
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        fast = dummy_head.next
        slow = dummy_head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = dummy_head.next
                while slow!=fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None




sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(8)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

head1 = ListNode(9)
head1.next = ListNode(7)
head1.next.next = ListNode(3)
head1.next.next.next= ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next= ListNode(6)

c = sol.getIntersectionNode(head,head1)
print(c.val)