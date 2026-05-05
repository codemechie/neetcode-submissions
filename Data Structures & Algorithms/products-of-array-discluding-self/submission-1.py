class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = list()
        for i in range(len(nums)):
            prod = 1
            j = 0
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    prod *= nums[j]
            results.append(prod)
        return results