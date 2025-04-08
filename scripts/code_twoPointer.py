

class Solution(object):
    # 344. 反转字符串
    def reverseString(self, s):
        left, right = 0,len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    # 代码随想录：替换数字
    def replaceNum(self,s):
        count = 0
        for c in s:
            if c <= '9' and c >= '0':
                count += 1
        res = [''] * (len(s) + count * 5)
        resLength = len(s) + count * 5 - 1
        slen = len(s) -1
        while slen >=0:
            if s[slen] <= '9' and s[slen] >= '0':
                res[resLength] = 'r'
                resLength -= 1
                res[resLength] = 'e'
                resLength -= 1
                res[resLength] = 'b'
                resLength -= 1
                res[resLength] = 'm'
                resLength -= 1
                res[resLength] = 'u'
                resLength -= 1
                res[resLength] = 'n'
                resLength -= 1
            else:
                res[resLength] = s[slen]
                resLength -= 1
            slen -= 1
        return ''.join(res)
    # 151.反转字符串中单词
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()

        left, right = 0, len(word) - 1
        while left < right:
            word[left],word[right] = word[right],word[left]
            left += 1
            right -= 1
        s = ' '.join(word)
        return s


sol = Solution()



