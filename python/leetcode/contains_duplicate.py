from typing import List


def containsDuplicate(nums : List[int]) -> bool:
    return len(nums) != len(set(nums))
    # next discussion point: how does set conversion in python work?
    # it's implemented as a hash table under the hood. 
    # Q: "so what happens if the elements are unhashable?" (like if they were a list)
    # A: well, this would raise a TypeError.
    # Q: "so what do you do then?"
    # A: Well, we would have to convert the elements to a hashable type (like tuple)...
    #    or we could sort the elements and check for duplicates using python's 'in'. 
    #    That'd be O(n log n) time, as sorting in python is O(n log n). 

# this works great, but turns out, no need to convert the set back to the list
def contains_duplicate_first(nums : List[int]) -> bool:
    return len(nums) != len(list(set(nums)))



if __name__ =="__main__":
    examples = [
        [[1,2,3,1], True],
        [[1,2,3,4], False],
        [[1,1,1,3,3,4,3,2,4,2], True]
    ]

    for lis, expected in examples:
        result = containsDuplicate(lis)
        assert result == expected, (f"failed for '{lis}' -- should be {expected}, not {result}.")
        print(f"✅ for test {lis}.")
    print("all tests passed.")