class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        #a permutation would be, in a row, so within that window size, those three exist
        table1 = {}
        for i in s1:
            if i not in table1:
                table1[i] = 1
            else:
                table1[i] += 1

        window1_size = len(s1)
        window2_size = len(s2)
        if window2_size < window1_size:
            return False

        table2 = {}
        left = 0
        # so look through this next string, from 0 to len   
        for right in range(window2_size):
   
            # if the tables are equal, the same keys with the same values
            table2[s2[right]] = table2.get(s2[right], 0) + 1

            if sum(table2.values()) > window1_size:
                while sum(table2.values()) > window1_size:
                    table2[s2[left]] -= 1
                    if table2[s2[left]] == 0:
                        del table2[s2[left]]
                    left += 1

            if table1 == table2:
                    return True

            #check if its the correct length
        return False