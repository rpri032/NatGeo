'''
Created on Sep 19, 2016

@author: RICH
'''
class Address:
    def __init__(self, streetAddress, city, postalCode, state, country):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country
        
    def __str__(self):
        return "{}, {} {} {}, {}".format(self.streetAddress, self.city, self.state, self.postalCode, self.country.upper())