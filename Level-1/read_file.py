import ast  # for safely evaluating strings like tuples and lists


def read_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Add quotes around string literals in FOOD_STORAGE and ENCLOSURES
    lines[3] = lines[3].replace('h', "'h'").replace('c', "'c'").replace('o', "'o'")
    lines[4] = lines[4].replace('h', "'h'").replace('c', "'c'").replace('o', "'o'")

    # Parse each line
    ZOO_DIMENSIONS = ast.literal_eval(lines[0])
    DRONE_DEPOT = ast.literal_eval(lines[1])
    BATTERY_CAPACITY = int(lines[2])
    FOOD_STORAGE = ast.literal_eval(lines[3])
    ENCLOSURES = ast.literal_eval(lines[4])
    DEADZONES = ast.literal_eval(lines[5])

    return ZOO_DIMENSIONS, DRONE_DEPOT, BATTERY_CAPACITY, FOOD_STORAGE, ENCLOSURES, DEADZONES

