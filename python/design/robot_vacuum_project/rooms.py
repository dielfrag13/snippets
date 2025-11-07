"""Reusable room generators for the robot vacuum visualizer.

Each room is represented as a list of lists of single-character strings.
Chars used:
  '#': wall (impassable)
  'X': object (impassable)
  '.': open floor
  ' ': open floor (alternate)

The module exports several named generators and a TEST_ROOMS dict for
quick import in demos/tests.
"""
from __future__ import annotations

import random
from typing import Dict, List, Optional, Tuple

Grid = List[List[str]]


def empty_room(rows: int, cols: int, border: bool = True) -> Grid:
    """Create an empty room (all open floor) with optional walls on border.

    Args:
        rows, cols: dimensions (>=3 recommended)
        border: whether to put '#' around the perimeter
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be > 0")

    grid: Grid = [["." for _ in range(cols)] for _ in range(rows)]
    if border and rows >= 2 and cols >= 2:
        for c in range(cols):
            grid[0][c] = "#"
            grid[rows - 1][c] = "#"
        for r in range(rows):
            grid[r][0] = "#"
            grid[r][cols - 1] = "#"
    return grid


def random_room(rows: int, cols: int, obstacle_prob: float = 0.12, seed: Optional[int] = None) -> Grid:
    """Create a random room with border walls and interior obstacles marked 'X'.

    obstacle_prob: probability each interior cell becomes 'X'.
    seed: optional randomness seed for reproducibility.
    """
    rng = random.Random(seed)
    grid = empty_room(rows, cols, border=True)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if rng.random() < obstacle_prob:
                grid[r][c] = "X"
    return grid


def narrow_corridor(length: int = 1, width: int = 5) -> Grid:
    """Create a narrow corridor room: width x length with walls around.

    The corridor will be oriented along rows (length rows, width cols)
    with a single opening at one end.
    """
    rows = max(3, length + 2)
    cols = max(3, width)
    grid = empty_room(rows, cols, border=True)
    # carve interior corridor ('.') across all interior cells
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            grid[r][c] = "."
    # Make an opening at bottom center
    mid = cols // 2
    grid[rows - 1][mid] = "."
    return grid


def checkerboard_room(rows: int, cols: int) -> Grid:
    """Create a room with a checkerboard pattern of open and small obstacles.

    Useful for testing coverage in constrained obstacle fields.
    """
    grid = empty_room(rows, cols, border=True)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if (r + c) % 2 == 0:
                grid[r][c] = "X"
            else:
                grid[r][c] = "."
    return grid


def spiral_room(size: int = 11) -> Grid:
    """Create a spiral-shaped open path inside walls.

    size: outer dimension (will be made odd if necessary).
    """
    n = max(5, size)
    if n % 2 == 0:
        n += 1
    grid = [["#" for _ in range(n)] for _ in range(n)]
    # carve a spiral path
    r = c = 1
    dr, dc = 0, 1
    steps = n - 2
    while steps > 0:
        for _ in range(steps):
            grid[r][c] = "."
            r += dr
            c += dc
        # step back
        r -= dr
        c -= dc
        # turn right
        dr, dc = dc, -dr
        r += dr
        c += dc
        if dc == 0:
            steps -= 1
    grid[1][1] = "."
    return grid


def concentric_rooms(layers: int = 3, layer_spacing: int = 2) -> Grid:
    """Create nested square rooms (concentric walls) useful for path planning.

    layers: number of enclosed layers (>=1).
    layer_spacing: spacing between walls.
    """
    size = 2 + layers * (layer_spacing + 1) * 2
    grid = [["." for _ in range(size)] for _ in range(size)]
    # fill with open then add concentric walls
    for layer in range(layers):
        offset = 1 + layer * (layer_spacing + 1)
        max_idx = size - 1 - offset
        for i in range(offset, max_idx + 1):
            grid[offset][i] = "#"
            grid[max_idx][i] = "#"
            grid[i][offset] = "#"
            grid[i][max_idx] = "#"
    return grid


def named_test_rooms() -> Dict[str, Grid]:
    """Return a dict of pre-built rooms for easy import and iteration."""
    rooms: Dict[str, Grid] = {}
    rooms["small_empty"] = empty_room(7, 9)
    rooms["medium_random"] = random_room(12, 16, obstacle_prob=0.12, seed=42)
    rooms["large_random"] = random_room(24, 36, obstacle_prob=0.10, seed=123)
    rooms["narrow_corridor"] = narrow_corridor(length=10, width=5)
    rooms["checkerboard"] = checkerboard_room(13, 13)
    rooms["spiral"] = spiral_room(15)
    rooms["concentric"] = concentric_rooms(layers=3, layer_spacing=1)
    return rooms


# module-level TEST_ROOMS for convenience
TEST_ROOMS: Dict[str, Grid] = named_test_rooms()


__all__ = ["Grid", "empty_room", "random_room", "narrow_corridor",
           "checkerboard_room", "spiral_room", "concentric_rooms",
           "named_test_rooms", "TEST_ROOMS"]
