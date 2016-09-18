'''
Created on Sep 17, 2016

@author: RICH
'''
class Address(object):
    def __init__(self, streetAddress, city, postalCode, country):
        self.streetAddress = streetAddress
        self.city = city
        self.postalCode = postalCode
        self.country = country
    def __str__(self):
        return "{}, {} {} {}".format(self.streetAddress, self.city, self.postalCode, self.country.upper())
    