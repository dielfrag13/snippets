from typing import List



def maxProfit(prices : List[int]) -> int:
    # main idea: any sell at day 'i' is only as good as the cheapest buy before it.
    # so we need to test if we sold today, what would our profit be?
    # [[1, 15, 10, 2, 9], 14]
    best_buy = prices[0]
    profit = 0
    for i, sell_value in enumerate(prices):
        if i == 0:
            continue
        if (sell_value - best_buy) > profit:
            profit = sell_value - best_buy 
        elif sell_value < best_buy:
            best_buy = sell_value
    return profit

def maxProfit_first(prices : List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    # choose a single day to buy one stock and choose a single different day to sell the stock.

    # enumerate through the list with first loop, first index is buy
    # enumerate through post-index list with second loop, index is sell
    # run through every combo of (sell - buy) and return highest value
    best = 0
    for bi, bp in enumerate(prices):
        for si, sp in enumerate(prices[bi+1:], start=bi+1):
            if (sp - bp > best):
                best = sp-bp

    return best


if __name__ == "__main__":
    testcases = [
        [[7,1,5,3,6,4], 5],
        [[7,6,4,3,1], 0],
        [[10, 2, 9, 1, 15], 14],
        [[1, 15, 2, 9, 1], 14],
    ]
    for testnums, expected in testcases:
        result = maxProfit(testnums)
        assert result == expected, (f"failed for nums={testnums}, expected={expected}. got result={result}")
    
    print("all example tests passed.")
