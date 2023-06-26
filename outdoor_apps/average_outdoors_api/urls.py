from django.urls import path
from . import views
urlpatterns = [
    path("conservation_area/", views.ConservationArea.as_view()),
    path("acitivty_pages/", views.ActivityPages.as_view()),
]