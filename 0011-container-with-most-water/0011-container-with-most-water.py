class Solution(object):
    def maxArea(self, height):
        li,ri=0,len(height)-1
        ma=0
        while li<ri:
            wi=ri-li
            y=0
            if height[li]<height[ri]:
                y=wi*height[li]
                li+=1
            else:
                y=wi*height[ri]
                ri-=1
            if y>ma:
                ma=y          
        return ma