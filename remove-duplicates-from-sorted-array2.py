# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


class Solution:
    def removeDuplicates(self, nums):

        # BaseCase
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):

            if slow == 1 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))  # 7
