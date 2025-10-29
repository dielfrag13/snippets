
"""LeetCode 1. Two Sum — template and tiny test harness.

Fill out or replace the implementation below as you practice.

Usage: run this file with Python to run the built-in example tests.
"""

from __future__ import annotations

from typing import List



def two_sum(nums: List[int], target: int) -> List[int]:
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	# there is an O(n) solution.
	# O(n) means the number of comparisons is a multiple of the number of elements.
	# it is not exponential. 
	seen = {}								# maps value -> its index
	for index, ele in enumerate(nums):
		need = target - ele
		if need in seen:
			return [seen[need], index]
		if ele not in seen:
			seen[ele] = index
	return []


def two_sum_second_attempt(nums: List[int], target: int) -> List[int]:
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	# version of the below, but that doesn't use an extra list

	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]

	return []





def two_sum_first_attempt(nums: List[int], target: int) -> List[int]:
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	# the basic, brute-force approach would be to start at the first index, check all others in front, 
	# calculating sums as we go. This is O(n^2) time complexity.

	# we will iterate through the entire list with i, and then create a subset list of elements
	# after the current i index. 

	for i in range(len(nums)):
		sublist = nums[i+1:]				# will always want to add 'i' to the j index to map back to i
		for j in range(len(sublist)):
			if nums[i] + sublist[j] == target:
				return [i, i + j + 1]

	return []



def two_sum_chatgpt(nums: List[int], target: int) -> List[int]:
	"""Return indices of the two numbers such that they add up to target.

	Args:
		nums: list of integers
		target: target integer

	Returns:
		A list with two indices [i, j] where i != j and nums[i] + nums[j] == target.

	Raises:
		ValueError: if no valid pair exists.

	Complexity:
		Time: O(n) using a hash map
		Space: O(n)
	"""
	# Simple hash-map approach: store value -> index
	seen: dict[int, int] = {}
	for i, num in enumerate(nums):
		complement = target - num
		if complement in seen:
			return [seen[complement], i]
		seen[num] = i

	raise ValueError("No two sum solution")


if __name__ == "__main__":
	# A few canonical examples you can run and modify.
	examples = [
		([2, 7, 11, 15], 9, [0, 1]),
		([3, 2, 4], 6, [1, 2]),
		([3, 3], 6, [0, 1]),
		([3, 3], 7, [])
	]

	for nums, target, expected in examples:
		result = two_sum(nums, target)
		# order of the two indices doesn't matter, accept either order
		assert result == expected or result == expected[::-1], (
			f"Failed for nums={nums}, target={target}. Got {result}, expected {expected}"
		)

	print("All example tests passed.")
