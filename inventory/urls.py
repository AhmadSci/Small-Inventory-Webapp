from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/", views.add_item_view, name="add"),
    path("update/<int:id>/", views.update_item_view, name="update"),
    path("search/", views.search_item_view, name="search")
]