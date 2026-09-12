class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Need to find delimeter #
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            # move to next char after delimeter 
            j += 1

            # Actual string
            res.append(s[j:j + length])

            # Move to the next length 
            i = j + length
        
        return res 
