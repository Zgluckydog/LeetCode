
class Solution(object):
    # 344.反转字符串
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        res = []
        for i in s:
            res.append(i)
        for i in range(len(s)):
            s[i] = res.pop()

    #  541. 反转字符串2
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0,len(s),2*k):
            if i+k <= len(s):
                s[i:i+k] = s[i:i+k:][::-1]
            else :
                s[i:len(s)] = s[i:len(s):][::-1]
        return "".join(s)
    # 代码随想录：替换数字
    def replaceNumbers(self):
        str = input().strip()
        oldIndex = len(str)-1
        count = 0
        for c in str:
            if c >= '0' and c <= '9':
                count += 1
        res = ['']*(len(str)+count*5)
        newIndex = len(res) - 1
        while oldIndex >= 0:
            if str[oldIndex] >= '0' and str[oldIndex] <= '9':
                res[newIndex] = 'r'
                newIndex -= 1
                res[newIndex] = 'e'
                newIndex -= 1
                res[newIndex] = 'b'
                newIndex -= 1
                res[newIndex] = 'm'
                newIndex -= 1
                res[newIndex] = 'u'
                newIndex -= 1
                res[newIndex] = 'n'
                newIndex -= 1
            else :
                res[newIndex] = str[oldIndex]
                newIndex -= 1
            oldIndex -= 1
        res = ''.join(res)
        print(res)
    # 151.反转字符串中单词
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()

        left,right = 0, len(word) - 1
        while left < right:
            word[left], word[right] = word[right],word[left]
            left+=1
            right-=1
        s = " ".join(word)
        return s
    # 代码随想录：右旋转字符串
    def rightReverse(self, k,s):
        s1 = s[:len(s)-k]
        s2 = s[len(s)-k:]
        res = s2+s1
        print(res)

    # 28. 找出字符串中第一个匹配项的下标
    def getNext(self,next,s):
        j = 0
        next[0] = j
        for i in range(1,len(s)):
            # 不匹配情况
            while j>0 and s[i]!=s[j]:
                j = next[j-1]
            # 匹配情况
            if s[i]==s[j]:
                j+=1
            next[i] = j

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        j = 0
        next = [0]*len(needle)
        self.getNext(next,needle)
        for i in range(len(haystack)):
            # 不匹配情况
            while j>0 and haystack[i]!=needle[j]:
                j = next[j-1]
            # 匹配情况
            if haystack[i] == needle[j]:
                j+=1
            # 找到长度符合情况
            if j==len(needle):
                return i - len(needle) + 1
        return -1
    # 459. 重复的子字符串
    def getNext(self, next, s):
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return False
        next = [0] * len(s)
        self.getNext(next, s)
        sLength = len(s)
        if next[sLength - 1] != 0 and sLength % (sLength - next[sLength - 1]) == 0:
            return True
        return False


sol = Solution()
# print(sol.reverseWords("the sky is blue"))
k = 2
s = "abcdefg"
sol.rightReverse(k,s)
