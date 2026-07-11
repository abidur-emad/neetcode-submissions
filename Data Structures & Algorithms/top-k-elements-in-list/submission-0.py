class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        for num in nums:
            buckets[num] = buckets.get(num, 0) + 1
        return [n for n, v in sorted(buckets.items(), key=lambda item: item[1], reverse=True)[:k]]
        