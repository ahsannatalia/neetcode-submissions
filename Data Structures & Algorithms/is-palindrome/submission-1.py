class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric char
        # for char in s:
        #     if not char.isalnum():
        #         s = s.replace(char, "")
        #     s = s.lower()
        # print(s)
    
        # for i in range(len(s)):
        #     start = i
        #     end = len(s)-1-i
        #     if s[start] != s[end]:
        #         return False
        #     if start == end:
        #         return True
        #     if end == 0 and start == len(s)-1:
        #         return True
        # return True
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while end > start and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start, end = start+1, end-1
        return True