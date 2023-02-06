from django.contrib import admin
from django.urls import path

appname = "userManagement"

urlpatterns = [
    # Register page
    path("register/", None, name="register"),
    
    # Login page
    path("login/", None, name="login"),
    
    # Logout page
    path("logout/", None, name="logout"),
    
    # User Info edit page
    path("edit/", None, name="edit"),
    
    # User Delete page
    path("delete/", None, name="delete"),
]