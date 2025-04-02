
class Solution(object):
    # 242.有效的字母异位词
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = [0] * 26
        for i in s:
            res[ord(i) - ord('i')] += 1
        for i in t:
            res[ord(i) - ord('i')] -= 1
        for i in res:
            if i:
                return False
        return True

    # 383.赎金信
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        res = [0] * 26
        for i in magazine:
            res[ord(i) - ord('a')] += 1
        for i in ransomNote:
            res[ord(i) - ord('a')] -= 1
        for i in res:
            if i < 0:
                return False
        return True
    # 49.字母异位词分组
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for str in strs:
            str_sort = sorted(str)
            str_key = "".join(str_sort)
            if str_key not in str_dict:
                str_dict[str_key] = []
            str_dict[str_key].append(str)
        return list(str_dict.values())
    # 438. 找到字符串中所有字母异位词
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if len(s)<len(p): return res
        s1 = [0]*26
        p1 = [0]*26
        for str in p:
            p1[ord(str)-ord('a')] += 1
        # 先确定第一个窗口
        for i in range(len(p)):
            s1[ord(s[i])-ord('a')] += 1
        if s1 == p1: res.append(0)
        # 后面窗口
        for i in range(len(p),len(s)):
            s1[ord(s[i-len(p)])-ord('a')] -=1
            s1[ord(s[i])-ord('a')] +=1
            if s1 == p1: res.append(i-len(p)+1)
        return res