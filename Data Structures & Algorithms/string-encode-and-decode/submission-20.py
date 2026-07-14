class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return "None"

        ret = ""
        for s in strs:
            ret += s + "||"

        return ret[:-2]

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []

        return s.split("||")