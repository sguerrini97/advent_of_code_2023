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


calibration = 0

digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

reversed_digits = {
    "orez": 0,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif" : 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}

def get_first_digit(line: str, digits: dict[str, int]) -> int:
    for i in range(0, len(line)):
        c = line[i]
        if c.isdigit():
            return int(c)
        elif parse_mode == 2:
            # If we are in part 2, we need to check for spelled digits
            for digit in digits.keys():
                if line[i:].startswith(digit):
                    return digits[digit]

with open(sys.argv[1]) as f:
    lines = f.readlines()

    for line in lines:

        first_digit = get_first_digit(line, digits)
        last_digit = get_first_digit("".join(reversed(line)), reversed_digits)

        line_calibration = str(first_digit) + str(last_digit)

        print(int(line_calibration))
        calibration += int(line_calibration)

print(f"Calibration: {calibration}")
