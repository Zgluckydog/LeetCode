class Solution(object):
    # 704
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            elif nums[mid] > target: right = mid - 1
        return -1
    # 35
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


sol = Solution()

print(sol.mySqrt(5))