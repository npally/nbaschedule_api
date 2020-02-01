from .models import Game
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import GameSerializer
import datetime


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows all games
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class TeamGameView(generics.ListAPIView):
    """
        This view returns all the games for a 
        specific team using input in the URL.
        """
    serializer_class = GameSerializer

    def get_queryset(self):
        
        team = self.kwargs['team']
        games = Game.objects.filter(home_team = team) | Game.objects.filter(away_team = team)
        print("The team is " + team)
        return games

class DateGameView(generics.ListAPIView):
    """
    Returns all games on a specific date.
    """
    serializer_class = GameSerializer

    def get_queryset(self):
        month = self.kwargs['month']
        day = self.kwargs['day']
        year = self.kwargs['year']    

        date = datetime.date(year, month, day)
        games = Game.objects.filter(date_time__date = date)
        return games