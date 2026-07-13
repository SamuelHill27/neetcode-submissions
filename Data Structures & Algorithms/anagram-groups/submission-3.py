class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in out:
                out[sorted_s] = [s]
            else:
                out[sorted_s].append(s)
            
        return list(out.values())