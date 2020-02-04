from django.urls import include, path
from rest_framework import routers

from .views import *



urlpatterns = [
    path("", AllGameView.as_view()),
    path("<int:pk>/", SingleGameView.as_view()),
    path("team=<str:team>/", TeamGameView.as_view()),
    path("date=<int:month>-<int:day>-<int:year>", DateGameView.as_view()),
    path("today", TodayGameView.as_view())
]