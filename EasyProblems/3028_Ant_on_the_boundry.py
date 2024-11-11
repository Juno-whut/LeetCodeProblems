class Solution:
    def returnToBoundaryCount(self, nums):
        boundry_counter = 0
        steps = 0
        for i in nums:
            steps += i
            if steps == 0:
                boundry_counter += 1
        return boundry_counter


def main():
    nums = [1, 2, 3, 4, 5]
    print(Solution().returnToBoundaryCount(nums))
    nums = [2, 3, -2, -3]
    print(Solution().returnToBoundaryCount(nums))
    nums = [9, -9, 6, -6]
    print(Solution().returnToBoundaryCount(nums))


if __name__ == "__main__":
    main()