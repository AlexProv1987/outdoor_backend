from django.urls import path
from . import views
urlpatterns = [
    path("conservation_area/", views.ConservationArea.as_view()),
]