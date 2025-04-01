from collections import defaultdict

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
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        res = [-1]*len(nums)
        resEnd = len(nums) - 1
        while left <= right:
            if nums[left]**2 < nums[right]**2:
                res[resEnd] = nums[right]**2
                right -=1
            else :
                res[resEnd] = nums[left]**2
                left += 1
            resEnd -= 1
        return res
    # 209. 长度最小的子数组
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        slowIndex = fastIndex = 0
        tempSum = 0
        subLength = 0
        res = float('inf')
        for fastIndex in range(len(nums)):
            tempSum+=nums[fastIndex]
            while tempSum >= target:
                subLength = fastIndex - slowIndex + 1
                tempSum -= nums[slowIndex]
                slowIndex+=1
                res = min(subLength, res)
        return res if res != float('inf') else 0
    # 904.水果成篮
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        slowIndex = fastIndex = 0
        res = defaultdict(int)
        maxLength = 0
        for fastIndex in range(0,len(fruits)):
            res[fruits[fastIndex]] += 1
            while len(res) > 2:
                res[fruits[slowIndex]] -= 1
                if res[fruits[slowIndex]] == 0:
                    res.pop(fruits[slowIndex])
                slowIndex += 1
            maxLength = max(fastIndex-slowIndex + 1,maxLength)
        return maxLength
    # 76.最小覆盖字串 （看不懂）
    # 59. 螺旋矩阵 II（生成螺旋数组不需要判断）
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        count = 1
        while left<=right and up <= down:
            # 填充上
            for i in range(left,right+1):
                res[up][i] = count
                count+=1
            up += 1
            # 填充右
            for i in range(up,down+1):
                res[i][right] = count
                count+=1
            right -= 1
            # 填充下
            for i in range(right,left - 1,-1):
                res[down][i] = count
                count+=1
            down -= 1
            # 填充左
            for i in range(down,up-1,-1):
                res[i][left] = count
                count+=1
            left += 1
        return res
    # 54. 螺旋矩阵(打印，需要判断后面两组是否还存在）
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
    # LCR 146. 螺旋遍历二维数组
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(array) == 0 or len(array[0]) == 0: return []
        left, right, up, down = 0, len(array[0]) - 1, 0, len(array) - 1

        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(array[up][i])
            up += 1
            for i in range(up, down + 1):
                res.append(array[i][right])
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    res.append(array[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    res.append(array[i][left])
                left += 1
        return res

sol = Solution()