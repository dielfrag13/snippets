from typing import Optional, List
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
def visit(tree : List[Optional[int]], start_index : int, reverse_visit : bool = False) -> List[Optional[int]]:
    # base case: outside of the range of the tree
    if start_index >= len(tree):
        return [None]
    l = visit(tree, (start_index*2 + 1), reverse_visit=reverse_visit)
    r = visit(tree, (start_index*2 + 2), reverse_visit=reverse_visit)
    if reverse_visit:
        return [tree[start_index]] + r + l
    return [tree[start_index]] + l + r



# optional means it can be type(x) or None. 
def isSymmetric(tree: List[Optional[int]]) -> bool:
    if not tree:
        return True
    return visit(tree, 1, reverse_visit = False) == visit(tree, 2, reverse_visit = True)

if __name__ =="__main__":
    examples2 = [
        [[1,2,2,3,4,4,3], True],
        [[1,2,2,None,3,None,3], False],
    ]
    examples = [
        # classic symmetric
        [[1,2,2,3,4,4,3], True],

        # asymmetric due to structure
        [[1,2,2,None,3,None,3], False],

        # empty tree is symmetric by definition
        [[], True],

        # single node
        [[1], True],

        # simple symmetric (just two children)
        [[1,2,2], True],

        # symmetric with inner None holes
        [[1,2,2,3,None,None,3], True],
        [[1,2,2,None,3,3,None], True],

        # asymmetric: value mismatch on mirrored positions
        [[1,2,2,3,None,None,4], False],
        [[1,2,2,3,4,5,3], False],

        # asymmetric: structure mismatch (missing mirrored child)
        [[1,2,2,None,2,None,2], False],

        # full level with same values (symmetric)
        [[1,2,2,2,2,2,2], True],

        # symmetric with different inner values but mirrored
        [[1,2,2,2,3,3,2], True],

        # only one child → not symmetric
        [[1,2], False],

        # extra node on one side deep
        [[1,2,2,None,None,None,3], False],

        # negatives/zeros, symmetric
        [[0,-1,-1,-2,None,None,-2], True],

        # asymmetric deeper mismatch
        [[1,2,2,None,None,2,3], False],
    ]

    for str, expected in examples:
        result = isSymmetric(str)
        assert result == expected, (f"failed for '{str}' -- should be {expected}, not {result}.")
        print(f"✅ for test {str}.")
    print("all tests passed.")