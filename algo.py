#!/usr/bin/env python3

import export_results
import parse_input
import types
import sys
import os

# Main body of the hashcode algorithm

def main():

    if len(sys.argv) != 2:
        print("Usage: {} <path-to-input-file>".format(sys.argv[0]))

    # Parse inputs
    input_f = sys.argv[1]
    if not os.path.isfile(input_f):
        raise FileNotFoundError

    # Process
    # TODO

    # Export results
    # TODO
    pass


if __name__ == "__main__":
    main()
