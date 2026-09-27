class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0

        maxstr = 0

        window = {}

        for right in range(len(s)):
            
            if s[right] not in window:
                window[s[right]] = 1
            
            elif s[right] in window:
                window[s[right]] += 1
            
            size = sum(window.values())
            # What is the window size?
            current_freq = max(window.values())
            # What is the most frequent character count?
            # How many replacements are needed to make the whole window one character?
            required = size - current_freq
            # Is the window valid? - should this be an if loop or a while loop?
            while required > k and left < len(s):
                window[s[left]] -= 1
                left += 1
                size = sum(window.values())
                # What is the window size?
                current_freq = max(window.values())
                required = size - current_freq

            maxstr = max(maxstr, sum(window.values()))
            
        return maxstr


        # so like 
        
        # a;1
        # b;2
        # c;1
        # as long as the total of all the numbers smaller than the largest is under k 







