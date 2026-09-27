class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        elif not s:
            return 0
        
        substr = set()

        left, right = 0, 1
        
        maxlen = 0
        substr.add(s[left])
        

        while right < len(s):
            
            # if its not in, add and move one to the right 
            if s[right] not in substr:
                substr.add(s[right])
                right+=1

            else:
                substr.remove(s[left])
                left+=1

            maxlen = max(maxlen, len(substr))  # current best


        return maxlen