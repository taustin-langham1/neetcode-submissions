class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ''
        for s in strs:
            word += str(len(s)) + '#' + s
        return word

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index('#', i) # find # from current i
            length = int(s[i:j]) # this will be the encoded number and hash
            word = s[j+1: j+1+length]
            result.append(word)
            i = j+1+length
        return result
        