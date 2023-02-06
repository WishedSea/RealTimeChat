from django.contrib import admin
from django.urls import path

appname = "userManagement"

urlpatterns = [
    # Register page
    path("register/", None),
    
    # Login page
    path("login/", None),
    
    # Logout page
    path("logout/", None),
    
    # User Info edit page
    path("edit/", None),
    
    # User Delete page
    path("delete/", None),
]