class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(map(lambda el : el + "|", strs))

    def decode(self, s: str) -> List[str]:
        return s.split('|')[:-1]