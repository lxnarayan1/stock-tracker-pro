from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('proj/', views.stock_detail, name="stock_detail"),
    path('autocomplete/', views.autocomplete, name="autocomplete"),
    path('favourites/', views.favourites_list, name="favourites"),
    path('favourites/add/<str:symbol>/', views.add_to_favourites, name="add_to_favourites"),
    path('favourites/remove/<str:symbol>/', views.remove_from_favourites, name="remove_from_favourites"),
    path("profile/", views.profile_view, name="profile"),

]