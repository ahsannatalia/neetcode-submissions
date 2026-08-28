class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for num in nums:
            if num not in dups:
                dups[num] = 1
            else:
                dups[num] += 1
        
        for x in dups.values():
            if x > 1:
                return True
        return False


        