import heapq
from collections import Counter
from typing import List


# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_dict = Counter(nums)

    heap = []

    for num, freq in freq_dict.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            if freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

    result = [item[1] for item in heap[::-1]]

    return result
