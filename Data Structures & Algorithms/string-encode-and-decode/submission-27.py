class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for word in strs:
            encoded += f"{len(word)}#{word}"

        return encoded

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i

            length = ""
            while s[j] != '#':
                length += s[j]
                j += 1

            length = int(length)
            res.append(s[j+1:j+length+1])
            
            i = j + 1 + length

        return res