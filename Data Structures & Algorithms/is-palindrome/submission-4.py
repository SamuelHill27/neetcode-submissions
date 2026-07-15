class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alpha = [c for c in s if c.isalnum()]
        s = "".join(only_alpha).lower()
        return s == "".join(list(reversed(s)))