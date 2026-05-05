import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        j = len(cleaned)-1
        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[j]:
                return False
            j-=1
        return True