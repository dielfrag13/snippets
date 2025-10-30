import string

def isPalindrome(s: str) -> bool:
    # this one is simple -- we have lots of pythonic tools at our disposal here
    # let's build a new string without grammar
    s = "".join([c for c in s if c not in string.punctuation+string.whitespace])

    # let's decapitalize it
    s = s.lower()

    # compare it to itself, reversed
    return s == s[::-1]

    # or run through with an indexer up to size/2 and check index, size-index for equality

    #return True



if __name__ =="__main__":
    examples = [
        ["A man, a plan, a canal: Panama", True],
        [" ", True],
        ["race a car", False],
    ]

    for str, expected in examples:
        result = isPalindrome(str)
        assert result == expected, (f"failed for '{str}' -- should be {expected}, not {result}.")
    print("all tests passed.")