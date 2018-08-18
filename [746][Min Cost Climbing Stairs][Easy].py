# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def minCost(cost):
            return min(minCost(cost[1:]),minCost(cost[2:])) +cost[0] if cost else 0
        return minCost([0]+cost)



class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        len_cost=len(cost)
        if (len_cost ==0)or(len_cost==1):return 0
        cum_cost=[0]*(len_cost+1)
        cum_cost[0],cum_cost[1]=cost[0],cost[1]
        cost.append(0)
        for i in range(2,len_cost+1):
            cum_cost[i]=min(cum_cost[i-2],cum_cost[i-1])+cost[i]
        return cum_cost[-1]



cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost=[10, 15, 20]
Solution().minCostClimbingStairs(cost)