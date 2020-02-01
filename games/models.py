from django.db import models
import csv
from datetime import datetime

CSV_FILE = "nba_games.csv"
# Create your models here.
class Game(models.Model):

    date_time = models.DateTimeField()
    away_team = models.CharField(max_length=50)
    away_rest = models.IntegerField()
    home_team = models.CharField(max_length=50)
    home_rest = models.IntegerField()
    arena = models.CharField(max_length=50)

    @classmethod
    def load_games(cls):
        with open(CSV_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dt = row['date'] + " " + row['start_est']
                dt_format = "%d-%b-%y %I:%M%p"
                date_time = datetime.strptime(dt, dt_format)
                away_team = row['away_team']
                away_rest = row['away_rest']
                
                if away_rest == 'first_game':
                    away_rest = 5
                else:
                    away_rest = int(away_rest)

                home_team = row['home_team']
                home_rest = row['home_rest']
                if home_rest == 'first_game':
                    home_rest = 5
                else:
                    home_rest = int(home_rest)

                arena = row['arena']

                game = Game(date_time=date_time, away_team=away_team, away_rest=away_rest, 
                            home_team=home_team, home_rest=home_rest, arena=arena)
                game.save()