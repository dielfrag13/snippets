from scaffolding import RoomVisualizer, RobotVacuum, Status
import rooms


# coordinates are in (row, col) format, which is the 
# returns forward coordinates, or backwards coords if backwards=True
def get_front_coords(robot, backwards=False):
	dir_idx = robot.dir_idx
	if backwards:
		dir_idx = (dir_idx + 2) % 4
	# facing north
	if dir_idx == 0: # facing north
		return (robot.r - 1, robot.c)
	if dir_idx == 1: # facing east
		return (robot.r, robot.c + 1)
	if dir_idx == 2:
		return (robot.r + 1, robot.c)
	if dir_idx == 3:
		return (robot.r, robot.c - 1)

def get_side_coords(robot, right=False):
	dir_idx = robot.dir_idx
	if right == True:
		dir_idx = (dir_idx + 2) % 4
	# facing north
	if dir_idx == 0: # facing north
		return (robot.r, robot.c - 1)
	if dir_idx == 1: # facing east
		return (robot.r - 1, robot.c)
	if dir_idx == 2:
		return (robot.r, robot.c + 1)
	if dir_idx == 3:
		return (robot.r + 1, robot.c)

def demo():
	# Available rooms: 
	# ['small_empty', 'medium_random', 'large_random', 'narrow_corridor', 'checkerboard', 'spiral', 'concentric']
	room_type = 'large_random'
	#room = rooms.TEST_ROOMS[room_type]
	room = rooms.random_room(24, 36, obstacle_prob=0.25, seed=2147483647)
	#room = rooms.empty_room(3,8)
	print("\nloaded room type:", room_type)
	print()
	# print("Available rooms:", list(rooms.TEST_ROOMS.keys()))

	viz = RoomVisualizer(room, title="Robot demo")
	robot = RobotVacuum(room, start=(1, 1), start_dir="E", visualizer=viz)

	# check status codes:
	#    ok = Status["OK"]
	#	 blocked = Status["BLOCKED"]
	"""
	seq = [
		("forward",),
		("forward",),
		("turn_right",),
		("forward",),
		("turn_left",),
		("forward",),
		("turn_left",),
		("forward",),
	]

	for action in seq:
		act = action[0]
		status = getattr(robot, act)()
		print(f"Action: {act:10s} -> {status}")
	"""

	# before moving, push where we were
	# we will pop the stack at the end

	visit_stack = []
	orientation_stack = []
	cleaned_stack = [(1,1)]
	checked_list = []

	#def push_orientation():
	#visit_stack.append((robot.r, robot.c, robot.dir_idx))
		
	
	# called upon reaching a brand new square.
	def visit():
		print(f"visiting new square: {(robot.r, robot.c)}")
		visit_stack.append((robot.r, robot.c))
		orientation_stack.append(robot.dir_idx)
		# check left
		if get_side_coords(robot) not in (visit_stack + cleaned_stack + checked_list):
			robot.turn_left()
			forward_coords = get_front_coords(robot)
			if forward_coords not in (visit_stack + cleaned_stack + checked_list):
				if robot.forward() == Status.OK:
					visit()
				else:
					checked_list.append(forward_coords)
					print("blocked!")
			else:
				print("already visited or cleaned the left square!")
			robot.turn_right()
		# check forward
		forward_coords = get_front_coords(robot)
		if forward_coords not in (visit_stack + cleaned_stack + checked_list):
			if robot.forward() == Status.OK:
				visit()
			else:
				checked_list.append(forward_coords)
				print("blocked!")
		else:
			print("already visited the forward square!")
		# check right
		if get_side_coords(robot, right=True) not in (visit_stack + cleaned_stack + checked_list):
			robot.turn_right()
			forward_coords = get_front_coords(robot)
			if forward_coords not in (visit_stack + cleaned_stack + checked_list):
				if robot.forward() == Status.OK:
					visit()
				else:
					checked_list.append(forward_coords)
					print("blocked!")
			else:
				print("already visited or cleaned the square!")
			# clean
			robot.turn_left()
		robot.clean()
		cleaned_stack.append((robot.r, robot.c))
		prior_orientation = orientation_stack.pop()
		print("restoring orientation")
		while (robot.dir_idx != prior_orientation):
			robot.turn_right()
		print("restoring location")
		robot.backward()
		if len(visit_stack) > 0:
			pass
			"""
			if visit_stack[-1] != get_front_coords(robot, backwards=True):
				print("backtracking assertion did not pan out!")
				import code
				code.interact(local=locals())
			"""
		else:
			print("your room is clean!")
	

	print("exit this shell to start simulation")
	import code
	code.interact(local=locals())
	try:
		visit()
	except KeyboardInterrupt:
		print("check stuff")
		import code
		code.interact(local=locals())


	print("\nControls: robot.turn_left(), robot.turn_right(), robot.forward(), robot.backward(), robot.clean()")
	print()
	import code
	code.interact(local=locals())


if __name__ == "__main__":
	demo()

"""Robot vacuum scaffold: Robot API + Matplotlib visualizer.

This module provides:
...
"""