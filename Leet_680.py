class Solution:
    def validPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        while s[0] == s[r]:
            s = s[1:-1]
            if len(s) < 2:
                return True
            r = len(s) - 1
            
        sl = s[:-1]
        r = len(sl) - 1
        while sl[0] == sl[r]:
            sl = sl[1:-1]
            if len(sl) < 2:
                return True
            r = len(sl) - 1
        
        sr = s[1:]
        r = len(sr) - 1
        while sr[0] == sr[r]:
            sr = sr[1:-1]
            if len(sr) < 2:
                return True
            r = len(sr) - 1
        
        return False
