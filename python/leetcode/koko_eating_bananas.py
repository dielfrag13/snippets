from typing import List
import math
def minEatingSpeed(piles: List[int], h: int) -> int:

    # base case: pile count == h.
    #if len(piles) == h:
    #    return max(piles)

    # guess and check, but binary search. 
    # formulate a lower bound of what k could be and an upper. 
    # lower bound (lb) would be the smallest amount she could eat to consume all bananas within h hours
    # if they were all in one pile.
    lb = math.ceil(sum(piles) / h)

    # upper bound (ub) would be fastest she could consume the piles if she ate all of them in one go.
    # that would be max(piles).
    ub = max(piles)

    # we will do binary search between lb and ub, up to when we have either lb or ub as the answer
    while (ub - lb) != 0:
        # g is guess
        g = (ub + lb) // 2 # explicitly round down
        # for banana count in each pile, divide by guess, round up
        total_chomps = sum([math.ceil(pile/g) for pile in piles])

        if total_chomps <= h:
            # then we may not have to eat so many bananas. g can be lower, lessen the bound.
            ub = g
        else:
            # then we need to eat at least g bananas, maybe more. 
            # need to add 1. 
            lb = g + 1
            
    
    return lb


if __name__ == "__main__":
    examples = [
        # Prompt baselines
        [[3,6,7,11], 8, 4],
        [[30,11,23,4,20], 5, 30],
        [[30,11,23,4,20], 6, 23],

        # Single-pile edges
        [[100], 4, 25],
        [[5], 10, 1],
        [[1], 1, 1],

        # Equal piles
        [[10,10,10,10], 4, 10],   # one per hour
        [[10,10,10,10], 8, 5],    # slower allowed with more hours

        # Many small piles (h == len)
        [[1,1,1,1,1,1,1,1], 8, 1],

        # Force k > 1 with h == len
        [[2,2,2,2,2,2,2,2], 8, 2],
        [[2,2,2,2,2], 5, 2],

        # High variance (corrected)
        [[3,6,7,11,15,20], 6, 20],   # h == len ⇒ k = max(piles)
        [[3,6,7,11,15,20], 10, 8],   # minimal k that fits in 10 hours

        # Large numbers
        [[1000000000, 1000000000], 2, 1000000000],
        [[1000000000, 1000000000], 3, 1000000000],

        # Generous hours → speed 1 possible
        [[1,2,3,4,5,6,7,8,9,10], 100, 1],

        # Tight but valid (h == len)
        [[9,8,7,6,5,4,3,2,1], 9, 9],
        [[1,100,1,1,1], 5, 100],

        # Misc tricky
        [[5,9,13], 5, 7],          # k=6 → 6h; k=7 → 5h (minimal)
        [[7,7,7,7,7], 7, 7],       # with extra hours, still need k=7
    ]

    for test, h, expected in examples:
        result = minEatingSpeed(test, h)
        assert result == expected, (f"failed for '{test}' and h={h} -- should be {expected}, not {result}.")
        print(f"✅ for test {test}.")
    print("all tests passed.")

