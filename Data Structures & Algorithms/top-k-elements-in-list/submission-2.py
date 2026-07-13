class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        out = []
        for _ in range(k):
            largest_key = max(counts, key=counts.get)
            out.append(largest_key)
            counts.pop(largest_key)
        
        return list(reversed(out))