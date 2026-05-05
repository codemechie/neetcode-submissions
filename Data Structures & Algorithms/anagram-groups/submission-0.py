class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in my_map:
                my_map[sorted_word].append(word)
            else:
                my_map[sorted_word] = [word]
        return list(my_map.values())

                
