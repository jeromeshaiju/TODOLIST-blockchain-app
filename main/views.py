import os

from django.shortcuts import render

contract_address = os.environ.get('CONTRACT_ADDRESS')

def home(request):
    return render(request, "todolist.html", {'contract_address': contract_address})

