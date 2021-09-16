from collections import deque
from time import strftime, gmtime


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_seconds(time_str):
    h, m, s = time_str.split(":")
    h = int(h) * 3600
    m = int(m) * 60
    s = int(s)
    return h + m + s


def get_time(seconds_int):
    return strftime("%H:%M:%S", gmtime(seconds_int))


robots = []
robots_input = input().split(";")

for robot in robots_input:
    robot_name, processing_time = robot.split('-')
    robots.append(Robot(robot_name, int(processing_time)))

start_time = input()
seconds = get_seconds(start_time)
products = deque()

while True:
    command = input()
    if command == "End":
        break

    products.append(command)


while products:
    curr_item = products.popleft()
    seconds += 1
    found_robot = False

    for robot in robots:
        if seconds >= robot.busy_until:
            robot.busy_until = seconds + robot.processing_time
            found_robot = True
            print(f"{robot.name} - {curr_item} [{get_time(seconds)}]")
            break
    if not found_robot:
        products.append(curr_item)
