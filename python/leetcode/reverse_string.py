from typing import List

def reverseString(s : List[str]) -> List[str]:
    ls = len(s)
    for i in range(ls // 2):
        s[i], s[ls-1-i] = s[ls-1-i], s[i]
    return s


if __name__ =="__main__":
    examples = [
        [["h","e","l","l","o"], ["o","l","l","e","h"]],
        [["H","a","n","n","a","h"], ["h","a","n","n","a","H"]],
    ]

    for str, expected in examples:
        result = reverseString(str)
        assert result == expected, (f"failed for '{str}' -- should be {expected}, not {result}.")
        print(f"✅ for test {str}.")
    print("all tests passed.")