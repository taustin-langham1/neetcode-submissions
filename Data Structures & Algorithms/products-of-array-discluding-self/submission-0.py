class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        n = len(nums)
        prefixArray = [0] * n
        postfixArray = [0] * n

        prefix = 1
        for i in range(n):
            if n == 0:
                prefixArray[i] = prefix
            else:
                prefix = prefix * nums[i]
                prefixArray[i] = prefix
        
        postfix = 1
        n = len(nums)
        for j in reversed(range(n)):

            postfix = postfix * nums[j]
            postfixArray[j] = postfix

        output = [0] * n

        for k in range(n):
            if k == 0:
                output[k] = 1 * postfixArray[k + 1] 
            elif k == n - 1:
                output[k] = prefixArray[k - 1] * 1 
            else:
                output[k] = prefixArray[k - 1] * postfixArray[k + 1]
            
        return output

