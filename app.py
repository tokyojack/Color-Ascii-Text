from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init() # For windows

def print_art(msg, color):
	# List of avaliable colors
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	# If the chosen color is not in the available list 
	if color not in valid_colors:
		color = "magenta" # Set's it the default color of "magenta"
		print(f"'{color}' is not a valid color, defaulting to Magenta")

	ascii_art = figlet_format(msg) 	# Creates the text-art
	colored_ascii = colored(ascii_art, color=color) # Colors it
	print(colored_ascii) # And prints

if __name__ == "main":
	msg = input("What would you like to print? ")
	color = input("What color? ")
	print_art(msg, color)