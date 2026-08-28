class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for char in s:
            if char not in check:
                check[char] = 1
            else:
                check[char] += 1
        
        for char in t:
            if char in check:
                check[char] -= 1
            else:
                check[char] = 1
        
        if all(value == 0 for value in check.values()):
            return True
        return False

        # for char, value in check.items():
        #     print(f"{char}: {value}")


        