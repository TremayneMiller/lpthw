# Functions and Files

from sys import argv

# assign script and input file to argv
script, input_file = argv

# Takes a file as parameter and Prints all contents of the file


def print_all(f):
    print(f.read())

# Start from the first line of the file


def rewind(f):
    f.seek(0)

# Base don line count, print a specific line


def print_a_line(line_count, f):
    print(line_count, f.readline())


# set the current file to the input file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now ley's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# set current line to the first line of the file
current_line = 1
print_a_line(current_line, current_file)

# increment the line, second line.
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# increment the line, third line.
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
