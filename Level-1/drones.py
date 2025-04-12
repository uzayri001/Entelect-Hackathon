from scipy.spatial import distance

class Drone:

    # Initialize the drone with the given parameters
    # battery_capacity: int - the battery capacity of the drone
    # onGround: bool - whether the drone is on the ground
    # foodType: str - the type of food the drone is carrying
    # currentLocation: tuple - the current location of the drone
    def __init__(self, battery_capacity: int, onGround: bool = True, foodType: str = None, currentLocation: tuple = None):
        self.battery_capacity = battery_capacity
        self.onGround = onGround
        self.foodType = foodType
        self.currentLocation = currentLocation

    # Take off the drone
    # This function will take the drone from the ground to the air
    # It will also set onGround to False
    def takeOff(self):
        self.onGround = False
        oldLocation = self.currentLocation
        self.currentLocation = (self.currentLocation[0], self.currentLocation[1], 50)
        self.battery_capacity -= distance.euclidean(oldLocation, self.currentLocation)

    # Land the drone
    # This function will take the drone from the air to the ground
    # It will also set onGround to True
    def land(self, newLocation: tuple):
        self.onGround = True
        oldLocation = self.currentLocation
        self.currentLocation = (newLocation[0], newLocation[1], newLocation[2])
        self.battery_capacity -= distance.euclidean(oldLocation, self.currentLocation)

    # Move the drone to a new location
    # This function will move the drone to a new location
    # Update current location to a given new location
    def move(self, newLocation: tuple):
        oldLocation = self.currentLocation
        self.currentLocation = (newLocation[0], newLocation[1], oldLocation[2])
        self.battery_capacity -= distance.euclidean(oldLocation, self.currentLocation)
    

    # Get the current location of the drone
    def getCurrentLocation(self):
        return self.currentLocation
    
    # Get the on ground status of the drone
    def getOnGround(self):
        return self.onGround
    
    # Get the food type of the drone
    def getFoodType(self):
        return self.foodType
    
    # Get the battery capacity of the drone
    def getBatteryCapacity(self):
        return self.battery_capacity
        
