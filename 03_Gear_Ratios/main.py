#!/usr/bin/env python3

import sys

# Check for input file argument
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <part>")
    sys.exit(1)

# Check for part argument
parse_mode = int(sys.argv[2])
if parse_mode not in [1, 2]:
    print(f"Invalid challenge part: {sys.argv[2]}")
    sys.exit(2)

# Parse input file
with open(sys.argv[1]) as f:
    lines = f.readlines()

    parts_sum = 0
    schematics: list[list[str]] = []

    for line in lines:
        schematics.append(list(line.strip()))
        pass

    def is_symbol(c: str) -> bool:
        return not c.isdigit() and c != "."

    side_len = len(schematics) # assyume schematics is a square matrix
    for i in range(0, side_len):

        digits = ""
        counts = False

        for j in range(0, side_len):

            c = schematics[i][j]

            # stop on non-digit characters
            if not c.isdigit():
                if counts and len(digits) > 0:
                    parts_sum += int(digits)
                digits = ""
                counts = False
                continue

            digits += c

            # skip if we already know this part counts
            if counts:
                continue

            adjacent_values = [
                # previous row
                schematics[i - 1][j - 1] if i != 0 and j != 0                       else ".",
                schematics[i - 1][j]     if i != 0                                  else ".",
                schematics[i - 1][j + 1] if i != 0 and j != side_len - 1            else ".",
                # current row
                schematics[i][j - 1]     if j != 0                                  else ".",
                schematics[i][j + 1]     if j != side_len - 1                       else ".",
                # next row
                schematics[i + 1][j - 1] if i != side_len -1 and j != 0             else ".",
                schematics[i + 1][j]     if i != side_len - 1                       else ".",
                schematics[i + 1][j + 1] if i != side_len - 1 and j != side_len - 1 else ".",
            ]

            adjacent_symbols = list(filter(lambda c: is_symbol(c), adjacent_values))
            if len(adjacent_symbols) > 0:
                counts = True
                continue

        if counts and len(digits) > 0:
            parts_sum += int(digits)

    print(parts_sum)

