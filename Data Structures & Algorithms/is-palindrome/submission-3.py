
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        withoutPunct = ''.join(ch.lower() for ch in s if ch.isalnum())
        if withoutPunct == withoutPunct[::-1]:
            return True
        return False