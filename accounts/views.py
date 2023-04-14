# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Add this line to log the user in

            return redirect(f"{reverse('current:index')}?username={username}")
        else:
            error_message = "Please enter a correct username and password. Note that both fields may be case-sensitive."
            return render(request, 'base.html', {'error_message': error_message})

    else:
        return render(request, 'base.html')
