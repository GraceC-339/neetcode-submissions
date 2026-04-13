class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search between 1 and maxk (max size of the pile)
        # find the smallest possible k which meet the condition

        end = max(piles)
        start = 1
        temp_res = end

        while start <= end:
            mid = (start + end) // 2
            hours = 0
            # calculate the hours
            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                temp_res = min(mid,temp_res)
                end = mid - 1
            
            if hours > h:
                start = mid + 1
            
        
        return temp_res

            
            


