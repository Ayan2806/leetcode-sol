class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Initialize candies array
        candies = [1] * n

        # Step 2: Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Sum the candies array
        return sum(candies)

# Example usage
if __name__ == "__main__":
    ratings1 = [1, 0, 2]
    ratings2 = [1, 2, 2]
    solution = Solution()
    print(solution.candy(ratings1))  # Output: 5
    print(solution.candy(ratings2))  # Output: 4
