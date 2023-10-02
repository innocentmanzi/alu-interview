#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
    Given a list of non-negative integers
    representing walls of width 1, calculate
    how muwh water will be retained after it rains
    """
    n = len(walls)
    if n == 0:
        return 0
    # Initialize two arrays to store maximum height on left and right sides of
    # each wall
    left_max = [0] * n
    right_max = [0] * n
    # Calculate maximum height on left side for each wall and store it in
    # left_max
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    # Calculate maximum height on right side for each wall and store it in
    # right_max
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])
    water = 0
    # Iterate through array one more time to calculate the amount of water
    # trapped between each wall
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]
    return water
