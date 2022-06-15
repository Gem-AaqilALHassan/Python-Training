import argparse

# Example 1: To find the sum of command-line arguments using argparse

# Initialize the Parser
parser = argparse.ArgumentParser(description ='Process some integers.')

# Adding Arguments
parser.add_argument('integers', metavar ='N',
					type = int, nargs ='+',
					help ='an integer for the accumulator')

parser.add_argument(dest ='accumulate',
					action ='store_const',
					const = sum,
					help ='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))

# Example 2: Program to arrange the integer inputs in ascending order

# Initializing Parser
parser = argparse.ArgumentParser(description ='sort some integers.')

# Adding Argument
parser.add_argument('integers',
					metavar ='N',
					type = int,
					nargs ='+',
					help ='an integer for the accumulator')

parser.add_argument(dest ='accumulate',
					action ='store_const',
					const = sorted,
					help ='arranges the integers in ascending order')

args = parser.parse_args()
print(args.accumulate(args.integers))
