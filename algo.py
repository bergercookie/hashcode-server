#!/usr/bin/env python3

from export_results import export_results
import os
from parse_input import parse_input
import sys
import custom_types
import time

# Main body of the hashcode algorithm

def main():

    if len(sys.argv) != 2:
        print("Usage: {} <path-to-input-file>".format(sys.argv[0]))
        exit(1)

    # Parse inputs
    input_f = sys.argv[1]
    if not os.path.isfile(input_f):
        raise FileNotFoundError()

    problem = parse_input(input_f)

    # Process

    # Export results
    outfile = "{}_{}".format(int(time.time()), input_f)
    export_results(problem, outfile)


if __name__ == "__main__":
    main()
