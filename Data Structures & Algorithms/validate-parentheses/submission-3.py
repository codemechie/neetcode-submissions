class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {"[": "]", "{": "}", "(": ")"}
        my_stack = list()
        for char in s:
            if char in ["[", "{", "("]:
                my_stack.append(my_map.get(char))
                continue
            elif len(my_stack) < 1:
                return False
            elif not char == my_stack.pop():
                return False
        if len(my_stack) > 0:
            return False
        return True 