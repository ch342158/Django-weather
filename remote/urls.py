# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

from django.urls import path

from . import  views
app_name = 'remote'
urlpatterns = [
    path("", views.index, name='index'),

]