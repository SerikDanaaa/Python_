class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        mx=0
        for i in gain:
            alt+=i
            if (alt>mx):
                mx = alt
        return(mx)   
        