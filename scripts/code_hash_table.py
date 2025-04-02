
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