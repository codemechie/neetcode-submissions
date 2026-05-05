class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = list()
        for s in strs:
            encoded.append(f"{len(s)}:{s}")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            colon = s.find(":", i)
            length = int(s[i:colon])
            start = colon + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded
