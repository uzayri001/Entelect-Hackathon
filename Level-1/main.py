from drones import Drone
import read_file
import sys


def main():
    try:
        # input file name
        file_name = input("Enter the file name: ")
        
        # Read and parse the input file
        ZOO_DIMENSIONS, DRONE_DEPOT, BATTERY_CAPACITY, FOOD_STORAGE, ENCLOSURES, DEADZONES = read_file.read_input(file_name)
        
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    
    # Create a drone object
    drone = Drone(BATTERY_CAPACITY, currentLocation=DRONE_DEPOT)

    depot = (DRONE_DEPOT[0], DRONE_DEPOT[1])

    # Create a priority queue of enclosures sorted by 4th value (descending)
    priority_enclosures = sorted(ENCLOSURES, key=lambda x: x[3], reverse=True)

    result = []

    # Convert FOOD_STORAGE list to dictionary for easier lookup
    storages = {item[3]: (item[0], item[1]) for item in FOOD_STORAGE}

    #Queue creation logic

    def canFeed(food,animal):
        return food == animal
    
    result.append(depot)
    while(priority_enclosures): # While queue is not empty
        # Check the food we need to get from the storage
        current_food = priority_enclosures[0][-1]
        result.append(storages[current_food])
        # While the drone can feed the animals with the food it has, add the animals into the run
        while priority_enclosures and canFeed(current_food,priority_enclosures[0][-1]):
            animal = priority_enclosures.pop(0)
            feeding = animal[:2]
            result.append(feeding)
        # Finally, go back to the next food storage
        result.append(storages[current_food])
    result.append(depot)
    print(result)

    
   


if __name__ == "__main__":
    main()

