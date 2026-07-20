class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1

        substring = str(list(range(len(s) + 1)))

        for r in range(len(s)):
            if s[r] in t:
                count = defaultdict(int)
                count[s[r]] += 1
                if count == t_count:
                    return s[r]
                l = r + 1
                while l < len(s):
                    if s[l] in t and t_count[s[l]] - count[s[l]] > 0:
                        count[s[l]] += 1
                    if count == t_count and len(substring) > l - r:
                        substring = s[r:l+1]
                    l += 1
        
        return (substring if len(substring) <= len(s) else "")