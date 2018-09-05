import string

class Restaurant():
    """Object that represents an establishment that serves food."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print('\nName:', string.capwords(self.restaurant_name), '\nCuisine:', self.cuisine_type.title())
        
    def open_restaurant(self):
        print(string.capwords(self.restaurant_name), 'is open')
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, number_served=1):
        self.number_served += number_served