# 232.用栈实现队列
from collections import deque


class MyQueue(object):
    def __init__(self):
        self.stackIn = []
        self.stackOut = []
    def push(self, x):
        self.stackIn.append(x)
    def pop(self):
        if self.empty(): return None
        if self.stackOut: return self.stackOut.pop()
        else:
            for _ in range(len(self.stackIn)):
                self.stackOut.append(self.stackIn.pop())
            return self.stackOut.pop()
    def peek(self):
        res = self.pop()
        self.stackOut.append(res)
        return res
    def empty(self):
        return not self.stackIn and not self.stackOut
# 225.用队列实现栈
class MyStack(object):
    def __init__(self):
        self.queueIn = deque()
        self.queueOut = deque()
    def push(self, x):
        self.queueIn.append(x)
    def pop(self):
        if self.empty(): return None
        while len(self.queueIn) > 1:
            self.queueOut.append(self.queueIn.popleft())
        res = self.queueIn.popleft()
        self.queueIn, self.queueOut = self.queueOut, self.queueIn
        while self.queueOut:
            self.queueOut.popleft()
        return res
    def top(self):
        res = self.pop()
        self.queueIn.append(res)
        return res
    def empty(self):
        return len(self.queueIn) == 0

class Solution(object):
    # 20.有效的括号
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0: return False
        res = []
        for c in s:
            if c == '(': res.append(')')
            elif c == '{': res.append('}')
            elif c == '[': res.append(']')
            elif len(res)==0 or c != res[-1]: return False
            else: res.pop()
        if len(res) == 0: return True
        else: return False
    # 1047. 删除字符串中的所有相邻重复项
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for c in s:
            if len(res)==0 or res[-1] != c: res.append(c)
            else : res.pop()
        ret = ''.join(res)
        return ret
    pass

sol = Solution()
s = "([])"

print(sol.isValid(s))