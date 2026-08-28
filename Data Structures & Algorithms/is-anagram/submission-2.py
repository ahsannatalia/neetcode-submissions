class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check = {}
        # for char in s:
        #     if char not in check:
        #         check[char] = 1
        #     else:
        #         check[char] += 1
        
        # for char in t:
        #     if char in check:
        #         check[char] -= 1
        #     else:
        #         check[char] = 1
        
        # if all(value == 0 for value in check.values()):
        #     return True
        # return False

        # for char, value in check.items():
        #     print(f"{char}: {value}")

        # check if not the same length
        if len(s) != len(t):
            return False
        
        s1, t1 = {}, {}

        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            t1[t[i]] = 1 + t1.get(t[i], 0)
        return s1 == t1


        