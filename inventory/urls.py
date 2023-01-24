from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/", views.add_item_view, name="add"),
    path("update/<int:id>/", views.update_item_view, name="update"),
    path("delete/<int:id>/", views.delete_item_view, name="delete"),
    path("remove/", views.remove_item_view, name="remove"),
]