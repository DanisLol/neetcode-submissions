class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        temp = 0
        for i in strs:
            temp = len(i)
            encoded_string += str(temp)
            encoded_string += "#"
            encoded_string += i
    
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #excludes index j so we get the number only
            decoded_strs.append(s[j + 1 : j + length + 1])
            i = j + 1 + length
        return decoded_strs





