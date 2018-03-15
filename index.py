from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init() # For windows

def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"
		print(f"'{color}' is not a valid color, defaulting to Magenta")

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)


msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)