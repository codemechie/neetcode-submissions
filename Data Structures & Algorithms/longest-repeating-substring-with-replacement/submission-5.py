class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        my_map = {}
        max_length = 0
    
        for right in range(len(s)):
            my_map[s[right]] = my_map.get(s[right], 0) + 1
            max_freq = max(max_freq, my_map[s[right]])
        
            while (right - left + 1) - max_freq > k:
                my_map[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right - left + 1)
    
        return max_length   