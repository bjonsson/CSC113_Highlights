# Brenda Jonsson 11/8/22
# Assignment 9
# (I had to change the name of the file in order to get the file read properly.)

# Select a Class from our book or use the Class you created in a previous assignment. The class must have
# at least 2 methods.

# Write a test case for your class. Test the 2 methods. Use the setUp() method so you don’t have to create
# a new instance of your class in each test method. Run your test case, and make sure both tests pass.


# My class from Lab 7. Please note that I had to adjust these classes to actually return something. The
# assert methods do not recognize printed statements. They need returned strings.

class Restaurant():
    """Stores the restaurant's name and its cuisine type."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and its cuisine type."""

        # I had to change these from "print" to "return." Please see note under "print_menu" child class function.

        return("The restaurant's name is " + self.restaurant_name + ". The cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Prints a message saying that the restaurant is open."""
        print("Entrez! Nous sommes ouverts! (We are open.)")


class IceCreamStand(Restaurant):
    """Inherits from Restaurant class. Prints ice cream flavors."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        """Initialize attributes of the parent class with "super". """
        super().__init__(restaurant_name, cuisine_type)

    def print_menu(self):

        testing_message = "123" # I had to add something for the function to return.
                                # Otherwise, regardless of what is printed, it will say that this returns "None."
                                # So I think there is no assert method for string matching printed statements.

        print("Our flavors include the following: " )
        for each in self.flavors:
            print(each)

        return testing_message


# Feeding list into child class
menu = IceCreamStand("Blomma Gelato", "ice cream", ["rose gelato", "violet gelato", "elderflower gelato",
                                                    "lavender gelato", "orange blossom gelato", "marigold gelato"])

# Calling child class
menu.print_menu()