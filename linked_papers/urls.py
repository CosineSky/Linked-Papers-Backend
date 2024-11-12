from django.urls import path

from . import views

urlpatterns = [
    path("search/<slug:keyword>/<int:page>", views.search, name="search"),

    path("essay/<int:essayId>/detail", views.detail, name="detail"),

    path("essay/<int:essayId>/cited", views.cited, name="cited"),

    path("essay/<int:essayId>/related", views.related, name="related"),

    path("essay/category/<slug:categoryName>", views.category, name="category"),
]