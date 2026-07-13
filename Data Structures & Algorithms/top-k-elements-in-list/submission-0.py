class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        mode_list = []
        for _ in range(k):
            mode_value = max(hashmap.values())
            mode_num = [n for n, v in hashmap.items() if v == mode_value]
            mode_list.append(mode_num[0])
            hashmap.pop(mode_num[0])
        
        return mode_list
