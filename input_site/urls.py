from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("register", views.register, name="register"),
    # path("logout", views.logout_view, name="logout"),
    # path("login", views.login_view, name="login"),
    # path("create", views.create, name="create"),

    # API routes
    

    # match all other pages, used by react router
]