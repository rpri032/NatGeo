from django.shortcuts import render
def indexView(request):
    context = {
        "firstName": "Richard",
        "lastName": "Priest"
    }
    return render(request, 'index.html', context)

from Models.Address import Address as AddressModel
from Services.Address import Address as AddressService
def searchView(request):
    address = AddressModel("1150 K Street", "Washington", "20005", "DC", "United States")
    test = AddressService.StoreAddress(address)
    context = {
        "firstName": "Richardx",
        "lastName": "Priest",
        "address": str(address)
    }
    return render(request, 'search.html', context)