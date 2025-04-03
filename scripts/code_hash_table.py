
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
    # 349. 两个数组的交集
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        inter_set = set1 & set2
        return list(inter_set)
    # 350. 两个数组的交集二
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = {}
        ret = []
        for i in nums1:
            res[i] = res.get(i,0) + 1
        for i in nums2:
            if res.get(i,0) > 0:
                ret.append(i)
                res[i] -= 1
        return ret
    # 202.快乐数
    def getSum(self,n):
        sum = 0
        while n:
            n,r = divmod(n,10)
            sum += r**2
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = set()
        while True:
            sum = self.getSum(n)
            if sum == 1: return True
            if sum in res:
                return False
            else:
                res.add(sum)
            n = sum
    # 1. 两数之和
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for index,value in enumerate(nums):
            temp = target - value
            if temp in res:
                return [index, res[temp]]
            else:
                res[value] = index
        return []
    # 454. 四数相加
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        res = dict()
        for a in nums1:
            for b in nums2:
                res[a+b] = res.get(a+b,0) + 1
        sum = 0
        for c in nums3:
            for d in nums4:
                if -(c+d) in res:
                    sum += res[-(c+d)]
        return sum
    # 15.三数之和
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: return result

            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]: left+=1
                    while left < right and nums[right] == nums[right-1]: right-=1
                    left+=1
                    right-=1
        return result
    # 18. 四数之和
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > target and target > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] > target and target > 0: break
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                left = k + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[k] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[k] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[k], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1
        return result



