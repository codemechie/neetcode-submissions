class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = dict()
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
        my_list = list()
        for _ in range(k):
            max_val = 0
            max_key = None
            for key, val in my_map.items():
                if val > max_val and key not in my_list:
                    max_val = val
                    max_key = key
            if max_key is not None:
                my_list.append(max_key)
        return my_list
            