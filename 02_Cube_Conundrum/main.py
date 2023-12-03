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

# Cubes config for part 1
config = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# Holds the sum of possible game IDs for part 1
possible_games = 0

# Holds the sum of the power of each set of cubes for part 2
power_sum = 0

# Parse input file
with open(sys.argv[1]) as f:
    for line in f:
        
        game = int(line.strip().split(":")[0].strip().split(" ")[-1])
        str_game_samples = line.strip().split(":")[1].strip().split(";")
        game_samples = []

        for samples in str_game_samples:
            str_samples = samples.strip().split(",")
            samples = {}
            for sample in str_samples:
                qty = int(sample.strip().split(" ")[0])
                color = sample.strip().split(" ")[1]

                samples[color] = samples.get(color, 0) + qty
            game_samples.append(samples)
        
        print(f"Game {game}: {game_samples}")

        # Check which games would be possible with the given config
        if parse_mode == 1:
            possible = True
            
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

        # Check the minimum number of cubes of each color needed for each game
        else:
            min_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for game_sample in game_samples:
                if game_sample.get("red", 0) > min_cubes["red"]:
                    min_cubes["red"] = game_sample.get("red", 0)
                if game_sample.get("green", 0) > min_cubes["green"]:
                    min_cubes["green"] = game_sample.get("green", 0)
                if game_sample.get("blue", 0) > min_cubes["blue"]:
                    min_cubes["blue"] = game_sample.get("blue", 0)
                pass

            cubes_power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
            power_sum += cubes_power

if parse_mode == 1:
    print(f"Possible games: {possible_games}")
else:
    print(f"Power sum: {power_sum}")
