# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

from django.apps import AppConfig


class RemoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'remote'
