# NBA Schedule API

## EndPoints
Root Endpoint: localhost:8000/games

### "/"
Returns all games from the NBA season
Example: localhost:8000/games/

### "/{gameid}"
Returns individual game object
Example: localhost:8000/games/25

### "/teams={team name}"
Returns all games for the given team.
Example: localhost:8000/games/teams=Houston Rockets

### "/date=mm-dd-yyyy"
Returns all NBA games on the given date.
Example: localhost:8000/games/date=01-01-2020

### "/today"
Returns all NBA games scheduled for today.
Example: localhost:8000/games/today