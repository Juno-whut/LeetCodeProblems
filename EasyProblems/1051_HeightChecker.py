# sort array
#return number of numbers that are not in the correct position  

class Solution:
    def quicleSort(self, heights, lo, hi):
        heightLen = len(heights)-1
        lo = 0
        hi = heightLen
        if Slo < hi:
            p = self.partition(heights, lo , hi)
            self.quicleSort(heights, lo, p-1)
            self.quicleSort(heights, p+1, hi)
        return heights


    def partition(self, heights, lo, hi):
        mid = (hi - lo) // 2
        for i in range(lo, hi):
            if heights[mid] < heights[lo]:
                heights[lo], heights[mid] = heights[mid], heights[lo]      
            if heights[hi] < heights[lo]:
                heights[lo], heights[hi] = heights[hi], heights[lo]
            if heights[hi] < heights[mid]:
                heights[mid], heights[hi] = heights[hi], heights[mid]
        return i + 1



def main():
    lo = 0
    hi = 1
    print(Solution().quicleSort([5,1,2,3,4], lo, hi))
    print(Solution().quicleSort([1,1,4,2,1,3], lo, hi))
    print(Solution().quicleSort([1,2,3,4,5], lo, hi))

    
if __name__ == "__main__":
    main()



"""
sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
"""