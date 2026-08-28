class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            lookingFor = target - nums[i]
            print(f"Looking for the number: {lookingFor}")
            for j in range(len(nums)):
                if nums[j] == lookingFor and i != j:
                    print("found")
                    return [i, j]
            