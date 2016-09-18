from django.shortcuts import render
def index(request):
    context = {
        'firstName': 'Richard',
        'lastName': 'Priest'
    }
    return render(request, 'index.html', context)
from Models.Address import Address as AddressModel
from Services.Address import Address as AddressService

def addressSearch(request):
    address=AddressModel("1150 K Street", "Washington DC", 20005, "United States")
    AddressService.StoreAddress(address)
    
    context = {
        'firstName': 'Richard',
        'lastName': 'Priest',
        'address': str(address)
    }
    return render(request, 'search.html', context)
