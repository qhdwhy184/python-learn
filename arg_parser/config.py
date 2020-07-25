import argparse

# Instantiate the parser
parser = argparse.ArgumentParser()

# Required positional argument
parser.add_argument('path')

# # Optional positional argument
# parser.add_argument('opt_pos_arg', type=int, nargs='?',
#                     help='An optional integer positional argument')
#
# # Optional argument
# parser.add_argument('--opt_arg', type=int,
#                     help='An optional integer argument')
#
# # Switch
# parser.add_argument('--switch', action='store_true',
#                     help='A boolean switch')

args = parser.parse_args()

print("config - Argument values:")
print(args.path)
# print(args.opt_pos_arg)
# print(args.opt_arg)
# print(args.switch)