from django.shortcuts import render

import random

# Create your views here.
def index(request):
    """Home page for Password Generator"""
    return render(request, 'password_generators/index.html')

def password(request):
    """Generate random password"""
    
    # Get the length of password
    length = int(request.GET.get('length', 14))

    lower_chars = list('abcdefghijklmnopqrstuvwxyz')
    upper_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    symbols = list('!@#$%^&*()')
    numbers = list('0123456789')

    # Check if request has uppercase on
    if request.GET.get('uppercase'):
        lower_chars.extend(upper_chars)
    
    # Check if the request has symbols
    if request.GET.get('special'):
        lower_chars.extend(symbols)

    # Check if the request has numbers
    if request.GET.get('numbers'):
        lower_chars.extend(numbers)

    # Variable to hold password
    thepassword = ""

    # Iterate and select random characters from list lower_chars
    for x in range(length):
        temp_password = ''
        thepassword += random.choice(lower_chars)

    context = {'password': thepassword}
    return render(request, 'password_generators/password.html', context)

# Function to tell something about yourself in the password generator page
def about(request):
    """Something about the creator of this website"""
    return render(request, 'password_generators/about.html')
