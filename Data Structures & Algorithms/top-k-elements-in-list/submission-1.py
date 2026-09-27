class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}

        for i in nums:
            if i in map:
                # add one to its value
                map[i] += 1
            else:
                # initialise it in the map and add 1 to its value
                map[i] = 1
        
        # want to sort value in ascending order and return the top k keys

        sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]