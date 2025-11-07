from scaffolding import RoomVisualizer, RobotVacuum
import rooms

def _demo():
	room = rooms.TEST_ROOMS['medium_random']
	print("Room set to 'medium_random'. Change it?")
	print("You can import rooms and select a different room map as such:")
	print("  room = rooms.TEST_ROOMS['room_name']")
	print("Available rooms:", list(rooms.TEST_ROOMS.keys()))
	import code
	code.interact(local=locals())

	viz = RoomVisualizer(room, title="Robot demo")
	robot = RobotVacuum(room, start=(1, 1), start_dir="E", visualizer=viz)

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

	# show a blocked / already cleaned example
	print("Attempting to move back into an already-cleaned cell:")
	robot.turn_left()
	robot.turn_left()
	print("Action: forward ->", robot.forward())
	print("Controls: robot.turn_left(), robot.turn_right(), robot.forward()")
	import code
	code.interact(local=locals())


if __name__ == "__main__":
	_demo()

"""Robot vacuum scaffold: Robot API + Matplotlib visualizer.

This module provides:
...
"""