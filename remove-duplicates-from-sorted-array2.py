class Solution:
    def removeDuplicates(self, nums):

        # BaseCase
        if not nums:
            return 0

        slow = 1
        count = 1
        FIXED_DUPLICATES = 2

        for fast in range(1, len(nums)):

            if nums[fast] == nums[slow - 1]:
                if count < FIXED_DUPLICATES:
                    nums[slow] = nums[fast]
                    slow += 1
                count += 1

            elif nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
                count = 1

        return slow


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))  # 7

# Submitted Successfully
