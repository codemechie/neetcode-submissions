class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = dict()
        for char in s:
            my_map[char] = my_map.get(char, 0) + 1
        for char in t:
            if char not in my_map:
                return False
            my_map[char] -= 1
            if my_map[char] < 0:
                return False
        return all(count == 0 for count in my_map.values()) 