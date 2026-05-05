class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        one=0 
        two=len(s) - 1
        while one<two:
            if s[one]!=s[two]:
                return False
            else:
                one += 1
                two -= 1 
        return True