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

cubes = [
    {
        "red": 12,
        "green": 13,
        "blue": 14,
    },
    {

    },
]

config = cubes[parse_mode - 1]

possible_games = 0

with open(sys.argv[1]) as f:
    for line in f:
        
        game = int(line.strip().split(":")[0].strip().split(" ")[-1])
        str_game_samples = line.strip().split(":")[1].strip().split(";")
        game_samples = []
        possible = True

        for samples in str_game_samples:
            str_samples = samples.strip().split(",")
            samples = {}
            for sample in str_samples:
                qty = int(sample.strip().split(" ")[0])
                color = sample.strip().split(" ")[1]

                samples[color] = samples.get(color, 0) + qty
            game_samples.append(samples)
        
        print(f"Game {game}: {game_samples}")

        for game_sample in game_samples:
            if config["red"] < game_sample.get("red", 0):
                possible = False
                break
            if config["green"] < game_sample.get("green", 0):
                possible = False
                break
            if config["blue"] < game_sample.get("blue", 0):
                possible = False
                break

        if possible:    
            possible_games += game

print(f"Possible games: {possible_games}")
