'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

def minCostClimbingStars(cost):
    top = len(cost)
    payment = [0] * top
    payment[0], payment[1] = cost[0], cost[1]
    # each index's payment would be a cost of this index plus minimum of two previous payments
    for i in range(2, top):
        payment[i] = cost[i] + min(payment[i-1], payment[i-2])
    # and there are two ways to reach top at the end: through top-1 index or top-2 index, 
    #       and we choose minimum among them
    return min(payment[top-1], payment[top-2])