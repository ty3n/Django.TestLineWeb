from django.urls import path, include
from . import views

urlpatterns= [
    path("", views.login_request, name="login"),
    # path('login/', views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    # path("<single_slug>", views.single_slug, name="single_slug"),
]
