class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in t:
            if s.find(letter) >= 0:
                s = s.replace(letter, "", 1)
            else:
                return False

        return True