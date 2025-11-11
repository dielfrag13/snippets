from __future__ import annotations
"""Robot vacuum scaffold: Robot API + Matplotlib visualizer.

This module provides:
- Status enum: return codes for the robot API
- RobotVacuum: the robot interface (turn_left, turn_right, forward)
- RoomVisualizer: Matplotlib-based visualizer that updates on each call

The demo at the bottom runs a few moves to show the API and visualization.
"""


import os
from enum import Enum
from typing import Optional, Sequence, Tuple, Set

try:
	import numpy as np
	import matplotlib
	if not os.environ.get("DISPLAY"):
		matplotlib.use("Agg")
	import matplotlib.pyplot as plt
	MATPLOTLIB_AVAILABLE = True
except Exception:
	MATPLOTLIB_AVAILABLE = False


class Status(Enum):
	OK = 0
	BLOCKED = 1
	OUT_OF_BOUNDS = 2
	ALREADY_CLEANED = 3


class RoomVisualizer:
	"""Simple visualizer for a room map.

	Characters in the room map:
	  '#': wall (impassable)
	  'X': object (impassable)
	  '.' or ' ': open space
	  'C': cleaned

	The visualizer will draw the grid and the robot's location and
	orientation. In headless mode (no DISPLAY) it saves frames to
	a `frames/` directory.
	"""

	COLOR_MAP = {
		"#": (0.0, 0.0, 0.0),  # black wall
		"X": (0.4, 0.4, 0.4),  # object
		".": (1.0, 1.0, 1.0),  # open
		" ": (1.0, 1.0, 1.0),
		"C": (0.7, 0.9, 1.0),  # cleaned (light blue)
	}

	DIR_TO_ANGLE = {"N": 90, "E": 0, "S": -90, "W": 180}

	def __init__(
		self,
		room_map: Sequence[Sequence[str]],
		title: str = "Room",
		save_dir: str = "frames",
		pause: float = 0.15,
	) -> None:
		self.room_map = [list(row) for row in room_map]
		self.rows = len(self.room_map)
		self.cols = len(self.room_map[0]) if self.rows else 0
		self.title = title
		self.save_dir = save_dir
		self.pause = pause
		self.frame = 0

		self.headless = not MATPLOTLIB_AVAILABLE or not os.environ.get("DISPLAY")

		if self.headless:
			os.makedirs(self.save_dir, exist_ok=True)
		else:
			self.fig, self.ax = plt.subplots(figsize=(self.cols * 0.6, self.rows * 0.6))
			self.ax.set_title(self.title)
			self.ax.set_xticks([])
			self.ax.set_yticks([])

	def _char_to_rgb(self, ch: str):
		return self.COLOR_MAP.get(ch, (1.0, 1.0, 1.0))

	def update(self, robot_pos: Tuple[int, int], robot_dir: str, cleaned: Set[Tuple[int, int]]):
		"""Redraw the current state.

		Args:
			robot_pos: (row, col)
			robot_dir: one of 'N','E','S','W'
			cleaned: set of (row, col) cleaned cells
		"""
		# update internal map with cleaned marks for display only
		disp = [[ch for ch in row] for row in self.room_map]
		for (r, c) in cleaned:
			if 0 <= r < self.rows and 0 <= c < self.cols and disp[r][c] not in ("#", "X"):
				disp[r][c] = "C"

		if not MATPLOTLIB_AVAILABLE:
			# Simple ASCII fallback
			lines = []
			for r, row in enumerate(disp):
				row_chars = []
				for c, ch in enumerate(row):
					if (r, c) == robot_pos:
						row_chars.append({"N":"^","E":">","S":"v","W":"<"}[robot_dir])
					else:
						row_chars.append(ch)
				lines.append("".join(row_chars))
			out = "\n".join(lines)
			path = os.path.join(self.save_dir, f"frame_{self.frame:04d}.txt")
			with open(path, "w") as f:
				f.write(out)
			print(f"Saved ASCII frame -> {path}")
			self.frame += 1
			return

		# Build RGB image
		img = np.ones((self.rows, self.cols, 3), dtype=float)
		for r in range(self.rows):
			for c in range(self.cols):
				img[r, c] = self._char_to_rgb(disp[r][c])

		self.ax.clear()
		self.ax.imshow(img, origin="upper")
		# keep square pixels so arrows and cells line up
		self.ax.set_aspect('equal')
		self.ax.set_title(self.title)
		self.ax.set_xticks([])
		self.ax.set_yticks([])

		# Draw robot as a red arrow pointing to current_dir
		rr, rc = robot_pos
		# row/col deltas (row increases downward); plotting coords are (x=col,y=row)
		dir_to_delta = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
		dr, dc = dir_to_delta.get(robot_dir, (0, 0))
		# scale arrow length relative to cell size; increase so it's visible
		scale = 0.45
		dx = dc * scale
		dy = dr * scale
		try:
			# FancyArrowPatch gives reliable arrowheads and rotates exactly with dx,dy
			from matplotlib.patches import FancyArrowPatch

			arrow = FancyArrowPatch((rc, rr), (rc + dx, rr + dy), arrowstyle='->',
					mutation_scale=24, color='red', linewidth=1,
					shrinkA=0, shrinkB=0, zorder=3, transform=self.ax.transData)
			self.ax.add_patch(arrow)
		except Exception:
			# final fallback: use a simple arrow (may be backend-dependent)
			try:
				self.ax.arrow(rc, rr, dx, dy, head_width=0.25, head_length=0.25,
						fc='red', ec='red', length_includes_head=True)
			except Exception:
				# last resort: small red dot
				self.ax.scatter([rc], [rr], c='red', s=200)

		# save or show
		if self.headless:
			path = os.path.join(self.save_dir, f"frame_{self.frame:04d}.png")
			self.fig.savefig(path, bbox_inches="tight")
			print(f"Saved frame -> {path}")
			self.frame += 1
		else:
			plt.pause(self.pause)
			self.frame += 1


class RobotVacuum:
	"""Robot API that operates on a 2D room map.

	The robot exposes three methods that match the API you described:
	  - turn_left() -> Status
	  - turn_right() -> Status
	  - forward() -> Status

	The robot keeps track of cleaned cells. If `forward()` would move into
	a cell already cleaned, it returns Status.ALREADY_CLEANED (so a
	higher-level planner can avoid revisiting).
	"""

	DIRS = ["N", "E", "S", "W"]
	DELTAS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

	def __init__(
		self,
		room_map: Sequence[Sequence[str]],
		start: Tuple[int, int] = (0, 0),
		start_dir: str = "N",
		visualizer: Optional[RoomVisualizer] = None,
		auto_clean_start: bool = True,
	) -> None:
		"""Create a RobotVacuum.

		Args:
			room_map: grid of characters ('#' walls, 'X' objects, '.' open)
			start: (row, col) start position
			start_dir: starting facing direction 'N','E','S','W'
			visualizer: optional RoomVisualizer to update after actions
			auto_clean_start: if True, mark the starting cell as cleaned
		"""

		self.room_map = [list(row) for row in room_map]
		self.rows = len(self.room_map)
		self.cols = len(self.room_map[0]) if self.rows else 0
		self.r, self.c = start
		assert 0 <= self.r < self.rows and 0 <= self.c < self.cols, "start out of bounds"
		self.dir_idx = self.DIRS.index(start_dir)
		self.cleaned: Set[Tuple[int, int]] = set()

		# optionally mark starting cell as cleaned
		if auto_clean_start and self.room_map[self.r][self.c] not in ("#", "X"):
			self.cleaned.add((self.r, self.c))

		self.visualizer = visualizer
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)

	@property
	def current_dir(self) -> str:
		return self.DIRS[self.dir_idx]

	def turn_left(self) -> Status:
		self.dir_idx = (self.dir_idx - 1) % 4
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)
		return Status.OK

	def turn_right(self) -> Status:
		self.dir_idx = (self.dir_idx + 1) % 4
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)
		return Status.OK

	def forward(self) -> Status:
		"""Move forward one cell in the current facing direction.

		Forward no longer automatically cleans. It only moves the robot.
		Returns Status.OK on success, or BLOCKED/OUT_OF_BOUNDS on failure.
		"""
		dr, dc = self.DELTAS[self.current_dir]
		nr, nc = self.r + dr, self.c + dc

		# bounds check
		if not (0 <= nr < self.rows and 0 <= nc < self.cols):
			return Status.OUT_OF_BOUNDS

		cell = self.room_map[nr][nc]
		if cell in ("#", "X"):
			return Status.BLOCKED

		# move (we allow moving into cleaned cells to support backtracking)
		self.r, self.c = nr, nc
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)
		return Status.OK

	def backward(self) -> Status:
		"""Move backward one cell (opposite of current facing direction).

		Useful for simple backtracking without changing facing direction.
		"""
		# opposite direction = rotate 180 degrees delta
		dr, dc = self.DELTAS[self.current_dir]
		nr, nc = self.r - dr, self.c - dc

		if not (0 <= nr < self.rows and 0 <= nc < self.cols):
			return Status.OUT_OF_BOUNDS

		cell = self.room_map[nr][nc]
		if cell in ("#", "X"):
			return Status.BLOCKED

		self.r, self.c = nr, nc
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)
		return Status.OK

	def clean(self) -> Status:
		"""Mark the current cell as cleaned. Returns ALREADY_CLEANED if it was cleaned before."""
		if (self.r, self.c) in self.cleaned:
			return Status.ALREADY_CLEANED

		if self.room_map[self.r][self.c] in ("#", "X"):
			# shouldn't happen: cleaning an impassable cell is a no-op (or treat as BLOCKED)
			return Status.BLOCKED

		self.cleaned.add((self.r, self.c))
		if self.visualizer:
			self.visualizer.update((self.r, self.c), self.current_dir, self.cleaned)
		return Status.OK
