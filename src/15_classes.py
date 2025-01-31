# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        s = f"Latitude: {self.lat}, Longitude: {self.lon}"
        return s

lat = LatLon(2, 3)
print(lat)
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        s = f"Name: {self.name}, Latitude: {self.lat}, Longitude: {self.lon}"
        return s

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        s = f"Name: {self.name}, Difficulty: {self.difficulty}, Sise: {self.size}, Latitude: {self.lat}, Longitude: {self.lon}"
        return s


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint1 = Waypoint("Catacombs", 41.705705, -121.51521)
print(waypoint1)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache1 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)


# Print it--also make this print more nicely
print(geocache1)
