"""
Key insight:
You can get to the nth stair from n-2th + 2, or n-1th + 1. So, this is fibonacci. 
Then we make it dynamic programming by using the memoization technique, as observed.  
"""
def climbStairs(n: int) -> int:
    memo = {1 : 1, 2: 2}
    
    def recurse(n):
        if n not in memo:
            memo[n] = recurse(n-1) + recurse(n-2)
        return memo[n]
    
    return recurse(n)

if __name__ == "__main__":
    # A few canonical examples you can run and modify.
    examples = [
        [1,1],
        [2,2],
        [3,3],
        [4,5],
        [5,8],
    ]

    for num, expected in examples:
        result = climbStairs(num)
        # order of the two indices doesn't matter, accept either order
        assert result == expected, (
            f"Failed for nums={num}. Got {result}, expected {expected}"
        )

        print(f"✅ for test {num}.")
    print("All example tests passed.")