from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # [73,74,75,71,69,72,76,73]
    day_counts = []
    # stack is used to store colder days and the index of the cold days
    # when we arrive at a warmer day, we pop off the stack until the current temp
    # isn't over the top-stack temp
    # then we have everything we need to calculate the number of days passed
    # given the index of the stack element temp and the current index
    stack = []
    prev_t = -1
    for cur_index, cur_t in enumerate(temperatures):
        day_counts.append(0)
        # base case
        if cur_index == 0:
            prev_t = cur_t
            continue
        # if it got strictly warmer...
        if cur_t > prev_t:
            day_counts[cur_index-1] = 1
            # get the top of the stack's temp
            while stack and cur_t > stack[-1][0]:
                _, top_ele_index = stack.pop()
                day_counts[top_ele_index] = cur_index - top_ele_index

        # it stayed same temp or got cooler. Push the prev day's info to the stack.
        else:
            stack.append((prev_t, cur_index-1))
        
        # last task: set the prev day's temp to today
        prev_t = cur_t


    return day_counts

"""
Concluding discussion about this solution:
Each index is pushed at most once and popped at most once, 
so this is an (amortized) O(n) monotonic-stack solution.

ChatGPT eloquently analyzed this as follows:

Each day either:
    * gets resolved immediately (distance 1), 
    * is never pushed, or
    * is pushed once (when the next day isn’t warmer) and later popped once (first warmer day).

Sum of pushes+pops ≤ 2n ⇒ O(n) time; stack size ≤ n ⇒ O(n) space.
"""

"""
The most 'correct' answer:

from typing import List

def dailyTemperatures(T: List[int]) -> List[int]:
    n = len(T)
    ans = [0] * n
    stack = []  # store indices of days with temps in a decreasing stack
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans

The stack is always monotonically decreasing. Temps can always be re-derived from indexes,
so we don't even worry about storing them. When you see a warmer temperature, you resolve 
all colder temps.
"""


if __name__ == "__main__":
    examples = [
        [[73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]],
        [[30,40,50,60], [1,1,1,0]],
        [[30,60,90], [1,1,0]],
    ]

    for test, expected in examples:
        result = dailyTemperatures(test)
        assert result == expected, (f"failed for '{test}' -- should be {expected}, not {result}.")
        print(f"✅ for test {test}.")
    print("all tests passed.")