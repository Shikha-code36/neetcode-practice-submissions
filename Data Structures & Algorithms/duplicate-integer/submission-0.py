class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains={}

        for i in range(len(nums)):
            if nums[i] in contains:
                return True
            else:
                contains[nums[i]]=i
        return False

        