# 123 hard 动态规划 问题只能进行两次股票交易
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1:

# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:

# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:

# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][j]表示在第i天操作了k次股票，j表示是否有股票
        # k可为0，1，2 次操作； j 可为1有股票，0无股票
        if not prices: return 0
        dp = [[[ 0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        for k in range(3):
            dp[0][k][0] = 0 # 没有买入股票
            dp[0][k][1] = -prices[0] # 买入股票

        for i in range(1, len(prices)):
            # 0次交易，不持有股票
            dp[i][0][0] = dp[i-1][0][0]
            # 没有操作股票， 持有股票： 刚买入股票 or 刚买入股票过几天
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            # 有一次股票交易，不持有股票 ：前几天已经卖出 or 已经卖出之后
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
            # 有一次股票交易， 持有股票：第二次买入股票， 第二次买入股票之后几天
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
            # 第二次教育，不持有股票：第二次买入股票已经卖出，第二次卖出之后
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
        end = len(prices) - 1
        return max(dp[end][0][0],dp[end][1][0],dp[end][2][0])



