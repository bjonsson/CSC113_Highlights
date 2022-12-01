# Brenda Jonsson 10/29/22
# Assignment 7

# Part A - Creating a Class

class ContainerGardening():
    """This class gives advice for how you can decorate plants in containers."""
    def __init__(self, outdoor, indoor, riparian):
        self.outdoor = outdoor
        self.indoor = indoor
        self.riparian = riparian

    def outdoor_plant(self):
        """Gives decorating advice for outdoor container plants."""
        print("Description: Gives decorating advice for outdoor container plants.")

        print("An outdoor " + self.outdoor + " can be decorated with large, inexpensive objects "
                               "like pretty rocks, or seashells on top of the soil or sand, or you "
                               "can paint the pot before planting.")



    def indoor_plant(self):
        """Gives decorating advice for indoor container plants."""
        print("Description: Gives decorating advice for indoor container plants.")

        print("An indoor " + self.indoor + " can be decorated with tiny plastic, wooden, or ceramic figurines, "
                              "or more expensive objects like crystals on top of the soil or sand.")



    def riparian_plant(self):
        """Gives decorating advice for aquatic plant containers."""
        print("Description: Gives decorating advice for aquatic plant containers.")

        print("A " + self.riparian + " can be decorated with aquarium figurines from the store, or boiled driftwood. "
                                "Avoid seashells or anything else that can change the pH of the water.")



class Orchids(ContainerGardening):
    """Inherits from ContainerGardening."""
    def __init__(self, outdoor, indoor, riparian, small_orchid, large_orchid):
        self.small_orchid = small_orchid
        self.large_orchid = large_orchid
        """Initializes attributes of the parent class."""
        super().__init__(outdoor, indoor, riparian)

    # Overrides the parent class
    def riparian_plant(self):
        """Orchids are never cultivated under water."""
        print("Description: Overrides the parent class for orchids.")
        print("Orchids are not aquatic plants.")

    def orchid_small(self):
        """Gives advice for decorating a small orchid plant."""
        print("Description: Gives advice for decorating a small orchid plant.")
        print("A " + self.small_orchid  + " can have a whimsical pot in an interesting shape 3D printed.")



    def orchid_large(self):
        """Gives advice for decorating a large orchid plant."""
        print("Description: Gives advice for decorating a large orchid plant.")
        print("A " + self.large_orchid + " can use a glazed ceramic pot with aeration holes in it over a plastic pot.")



# Part A - Continued
# Make a class for something you would like to model. Make a class. Create at least 3 attributes.
# Make an init method as well as at least 2 other methods that make sense for your class. Create
# at least 2 different instances and test your methods using your different instances.

container_gardening = ContainerGardening("dragon fruit tree", "cactus", "Java fern")

container_gardening.outdoor_plant()
print() # Creates a new line.
container_gardening.indoor_plant()
print()
container_gardening.riparian_plant()
print()

# Part B - Inheritance
# Create a specialized version of the class in part A. It should have two new attributes. Make an init
# method as well as at least 1 other method. Override one of the methods from the parent class.
# Create at least 2 instances representing different objects which test your methods.

orchids = Orchids("dragon fruit tree", "cactus", "Java fern", "masdevallia", "phalaenopsis")

orchids.riparian_plant()
print()
orchids.orchid_small()
print()
orchids.orchid_large()
print()

# Part C - Objects and Lists
# Add all of your objects to a list.

container_gardening = ContainerGardening("dragon fruit tree", "cactus", "Java fern")
orchids = Orchids("dragon fruit tree", "cactus", "Java fern", "masdevallia", "phalaenopsis")

plant_list = [container_gardening.outdoor_plant(),
container_gardening.indoor_plant(),
container_gardening.riparian_plant(),
orchids.riparian_plant(),
orchids.orchid_small(),
orchids.orchid_large()]

# Iterate through your list and display descriptive information about each of your objects.

for each in plant_list:
    each
