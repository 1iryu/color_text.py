import os
import random

os.system('')


def rgb(x, y, z):
	return f'\x1b[38;2;{x};{y};{z}m'


def print_with_color(text: str, x, y, z):
	value = rgb(x, y, z)
	print(f"{value}" + text , end="")

#example
for i in range(10000):
	x = random.randint(0, 255)
	y = random.randint(0, 255)
	z = random.randint(0, 255)
	print_with_color("@", x, y, z)
