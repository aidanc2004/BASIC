#!/usr/bin/python3

# --------------------------- #
# Aidan Carey, June 29th 2024 #
# --------------------------- #

# Dict of variable names to values
variables = {}

# List of line numbers and expressions
lines = []

# Parse a line and add it to the list of lines
def parse(line):
  global lines
  
  words = line.split(" ")

  # Get line number from first word
  try:
    number = int(words.pop(0))
  except ValueError:
    print("Error: First word must be a line number.")
    return -1

  # Add the line and sort the list
  lines.append((number, words))
  lines.sort()

def run():
  i = 0
  
  while True:
    # If the index is out of range then the END keyword
    # wasn't found, so just terminate the program
    try:
      (number, expr) = lines[i]
    except IndexError:
      return

    # Don't do anything if it's empty
    if expr == []:
      i += 1
      continue;
    # Terminate the program
    if expr[0] == "END":
      return
    # Print out a string
    if expr[0] == "PRINT":
      # TODO: Only one argument which is a string
      args = expr[:] # Pass by value
      args.pop(0)
      print(" ".join(args))
    
    i += 1

# List the lines in the program
def list_program():
  for i in range(len(lines)):
    (number, expr) = lines[i]
    print(str(number) + " " + " ".join(expr))
    
# Main loop
while True:
  line = input();

  # Don't do anything on a blank line
  if line == "":
    continue
  # Run the program
  elif line == "RUN":
    run()
  # List out the lines in the program
  elif line == "LIST":
    list_program()
  # Parse the line
  else:
    parse(line);
