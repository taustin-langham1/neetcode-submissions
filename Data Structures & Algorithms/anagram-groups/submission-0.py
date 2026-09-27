class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for s in strs:
            
            key = ''.join(sorted(s)) # make key hashable

            if key not in hash_map: # if we haven't seen this list of chars
                hash_map[key] = [] # make this str a key, and its value an empty list

            hash_map[key].append(s) # and append the original string s to this list
        
        return list(hash_map.values()) # return the values of the hashmaps, which are our original strings grouped 

