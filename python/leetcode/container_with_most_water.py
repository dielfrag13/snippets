# first leetcode medium
from typing import List

def maxArea(heights: List[int]) -> int:

    # two dimensions to consider, sourced from:
    # * min(bar1height, bar2height)
    # * bar2index-bar1index
    # maximize for the multiplication of the two
    # the O(n^2) answer is to go from 1..len(heights)-1, and 
    # identifying the min of the bars separated by the current height
    # but we're not here to do the O(n^2) answer!!!!!!!!!1111

    # this is a two pointers problem. try to 'always move the pointer that points to the lowest line'. 
    # after debugging a pesky bug, i figured this out:
    pl = 0
    pr = len(heights) - 1
    best_area = -1   
    while pl != pr:
        plh = heights[pl]
        prh = heights[pr]
        area = (pr - pl) * min(plh, prh)
        if area > best_area:
            best_area = area
        # move the pointer to the lowest bar
        if plh > prh:
            pr -= 1
        else:
            pl += 1

    # the key insight: we have two dimensions, the distance bewteen bars, and the height of the bars.
    # Every iteration, we will lose one width, lessening area. However, in switching bars, we may
    # get a better, higher bar. Switching from the tallest bar will only negatively impact us, as it
    # may result in an even shorter bar. however, switching from the shorter bar may positively impact us
    # as it may grow in height faster than the loss in width. This is the key insight.
    return best_area


if __name__ == "__main__":

    examples = [
        # classic example — optimal between heights[1]=8 and heights[8]=7 (width 7 → 7*7=49)
        [[1,8,6,2,5,4,8,3,7], 49],
    #]
    #examples2 = [
        # smallest non-trivial input
        [[1,1], 1],
        
        # strictly increasing heights (best container uses first and last)
        [[1,2,3,4,5,6,7,8,9,10], 25],  # between 5 and 10 (width 5, height 5)
        
        # strictly decreasing heights (best container also between first and last)
        [[10,9,8,7,6,5,4,3,2,1], 25],
        
        # plateau case
        [[4,4,4,4,4], 16],  # between 0 and 4 → 4 * 4
        
        # valley shape — local minima in middle shouldn’t mislead algorithm
        [[2,3,10,5,7,8,9], 36],  # between heights[2]=10 and heights[6]=9 (width 4)
        
        # symmetric hill
        [[1,3,2,5,25,24,5], 24],  # between 25 and 24 (width 1 * height 24)
        
        # equal high edges, low middle
        [[10,1,1,10], 30],  # between both 10s (width 3 * height 10)
        
        # single peak in middle — must pick left/right edges
        [[1,2,4,3], 4],  # between 2 and 4 (width 1 * height 2) or 1 and 3 (width 3 * height 1)
        
        # flat zeros (trivial)
        [[0,0,0,0], 0],
        
        # one large number at one end
        [[100,1,1,1,1], 4],  # only width matters since right side small
    ]


    for bars, expected_area in examples:
        result = maxArea(bars)
        assert result == expected_area, (f"result area {result} doesn't match expected {expected_area}!")
        print(f"✅ for {bars} & max area {expected_area}")

    print("all tests passed.")