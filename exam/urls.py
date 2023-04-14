# Copyright (c) 2023 Final, All rights reserved.
# Created by Yongji Chen 400168246 for PROCTECH 4IT3.
# SoA Notice: I, Yongji Chen, certify that this material is my original work.
# I certify that no other person's work has been used without due acknowledgement.
# I have also not made my work available to anyone else without their due acknowledgement.

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views
from accounts.views import login_view  # Update the import statement here

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path('current/', include('current.urls')),
    path("remote/", include('remote.urls')),
    path('login/', login_view, name='login_view'),  # Update the URL pattern here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
