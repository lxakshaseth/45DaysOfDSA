class Solution:
    def trap(self, height: list[int]) -> int:
        
        # BEST Solution: 2 Pointer approach
        if not height:
            return 
        
        n = len(height)
        l =0 ; r = n-1 # Initialize the 2 pointers
        lMax = height[l]; rMax = height[r] # intialize the max pointers
        res = 0 # result accumalator (total trapped water)

        while l<r:
            if lMax <= rMax: # move pointer of side of lesser Max value
                l += 1 # lMax smaller ->  move left pointer
                lMax = max(lMax, height[l]) # V.IMP: update instantly avoids -ve sum
                res += lMax - height[l] # add to accumalator
                
                # we upadte lMax just after moving so worst case we add 0 to res no negative value as -ve only possible when height at l > lMax but that was handled using lMax comparison right after incrementing
            
            else: # Case were rMax is smaller
                r -= 1 # move r pointer
                rMax = max(rMax , height[r]) # update rMax, discussd why needed.
                res += rMax -height[r] # add the trapped water at this point
        
        return res # return total trapped water