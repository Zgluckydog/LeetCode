class Solution(object):
    # 704. 两数之和
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            elif nums[mid] > target: right = mid - 1
        return -1
    # 35. 搜索插入位置
    def searchInsert(self, nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return left
    # 34.在排序数组中查找元素的第一个和最后一个位置
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 分别找左边界和边界
        left = 0
        right = len(nums) - 1
        border_left = -1
        border_right = -1
        while left<= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                border_left = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        left = 0
        right = len(nums) - 1
        while left<= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                border_right = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return [border_left,border_right]
    # 69.x 的平方根
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x - 1
        res = 0
        while left <= right:
            mid = left + (right -left)//2
            if mid*mid <= x:
                left = mid + 1
                res = mid
            else :
                right = mid - 1
        return res
    # 367.有效的完全平方数
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num ==0 : return True
        left = 0
        right = num - 1
        while left <= right:
            mid = left + (right - left)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid + 1
            elif mid * mid >num:
                right = mid - 1
        return False
    # 27. 移除元素
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fastIndex = 0
        slowIndex = 0
        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex +=1
            fastIndex +=1
        return slowIndex
    # 26. 删除有序数组中的重复项
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fastIndex = 1
        slowIndex = 1
        while fastIndex < len(nums):
            if nums[fastIndex-1] != nums[fastIndex]:
                nums[slowIndex] = nums[fastIndex]
                slowIndex+=1
            fastIndex+=1
        return slowIndex
    # 283. 移动零
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1: return nums
        fastIndex = slowIndex = 0
        while fastIndex<len(nums):
            if nums[fastIndex]!=0:
                nums[slowIndex] = nums[fastIndex]
                slowIndex+=1
            fastIndex +=1
        for i in range(slowIndex,len(nums)):
            nums[i] = 0
        return nums
    # 844.比较含退格的字符串
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = []
        for c in s:
            if c != '#':
                res.append(c)
            elif len(res)!=0:
                res.pop()
        s = ''.join(res)

        res = []
        for c in t:
            if c != '#':
                res.append(c)
            elif len(res)!=0:
                res.pop()
        t = ''.join(res)
        return s == t
    # 977. 有序数组的平方

sol = Solution()

s = "ab#c"
t = "ad#c"
print(sol.backspaceCompare(s, t))