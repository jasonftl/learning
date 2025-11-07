# 26 July 2025
from typing import List

class Solution:
    def mccs(self, cost: List[int]) -> int:
        number_of_steps = len(cost)
        
        # Dynamic programming array where dp[i] represents 
        # the minimum cost to reach position i
        dp = [0] * (number_of_steps + 1)
        
        # Base cases: we can start at position 0 or 1 for free
        dp[0] = 0  # Free to start at position 0
        dp[1] = 0  # Free to start at position 1
        
        # Fill the dp array for each position from 2 onwards
        for current_position in range(2, number_of_steps + 1):
            # To reach current position, we can come from either:
            # 1. Previous position (pay its cost to leave it)
            # 2. Two positions back (pay its cost to leave it)
            cost_from_previous_position = dp[current_position - 1] + cost[current_position - 1]
            cost_from_two_positions_back = dp[current_position - 2] + cost[current_position - 2]
            
            # Take the minimum of both options
            dp[current_position] = min(cost_from_previous_position, cost_from_two_positions_back)
        
        print(dp)
        # Return the minimum cost to reach the top (position number_of_steps)
        return dp[number_of_steps]

if __name__ == "__main__":
    solution = Solution()
   
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3 = [0, 1, 2, 2]
    
    print(solution.mccs(cost1))  # Expected: 15
    print(solution.mccs(cost2))  # Expected: 6
    print(solution.mccs(cost3))  # Expected: 2