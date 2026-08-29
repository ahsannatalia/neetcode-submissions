class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric char
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
            s = s.lower()
        print(s)
    
        for i in range(len(s)):
            start = i
            end = len(s)-1-i
            if s[start] != s[end]:
                return False
            if start == end:
                return True
            if end == 0 and start == len(s)-1:
                return True
        return True