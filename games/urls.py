from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("team=<str:team>/", TeamGameView.as_view()),
    path("date=<int:month>-<int:day>-<int:year>", DateGameView.as_view()),
]