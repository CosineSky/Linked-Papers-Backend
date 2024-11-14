from django.urls import path
from . import views

urlpatterns = [
    path("search/<slug:keyword>/<int:page>", views.search, name="search"),

    path("paper/<int:essayId>/detail", views.detail, name="detail"),

    path("paper/<int:essayId>/cited", views.cited, name="cited"),

    path("paper/<int:essayId>/related", views.related, name="related"),

    path("paper/<int:essayId>/category/<int:page>", views.category, name="category"),
]