class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        res = []

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        pairs = list(frequencies.items())
        pairs.sort(key=lambda pair: pair[1])

        while k > 0:
            res.append(pairs.pop()[0])
            k -= 1

        return res