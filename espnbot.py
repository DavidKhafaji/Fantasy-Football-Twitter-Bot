import tweepy as tp
import requests
from bs4 import BeautifulSoup as bs
import os
from espn_api.football import League

team_to_nickname = {
    "Team(Concreatures)" : "Faji",
    "Team(Suga Sean's Hook)" : "Nick",
    "Team(Ft. Lauderdale Shark)" : "John",
    "Team(Hasbulla Hive)" : "CJ",
    "Team(# NewUs)" : "David",
    "Team(Free 5's)" : "Edson",
    "Team(Team Fants)" : "Nate",
    "Team(Mitchell)" : "Mitch",
    "Team(Diggs In A Blanket)" : "Matt",
    "Team(O.J.'s Running)" : "Brendan",
    "Team(Post Mahomes)" : "Jason",
    "Team(Long Live Football)" : "Tyler"
}


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKZTWQEAAAAApVoHlKBsPsbNbRe%2FTZM5E61Rnys%3DlH9VVfn6kSUkUmNEonZWlIU3uSRUeigQD7BzWvDBOpcXgKWlfV'
auth = tp.OAuthHandler("2lSOCXCTXeLS9XxYDuxv18rWg", "HhjNRrDY7P0uK0IXkKcr8HllRdfIl60AW5bjq5hmHMrS541iM0")
auth.set_access_token("1465529313638424580-dwXRXlfCXHtJArROhN8cuDhYsrvgqb", "ivlTivHl4ZcOvLXrdEpNa45YGfIFuvnQqxVGEUkltTUpF")
api = tp.API(auth)

league = League(league_id=204259, year=2022, espn_s2='AEBElm5duTifgyM8vT1lppHzm1Nx8iOVSugonXFZoHN89oqd%2Bd5yH6PsEXmztFvnxkoztoLsHb54%2BKnFKMhCw7n0DMVVSA7eXlBEOVTMcpg9hOz6SKhKCIOA%2FC%2BBSaJWiRBoIFemLDxyOqdoOrUrScTjw5zw%2FwunkYXSjRNJyKncMF5lSU90y6XA65Zfrf9eXLWmB8GbOT3cTgMKa9RSE3ys0i%2BKIfnH%2FgA%2B0wtoj5frkLaDlbwERrfqCRTbh%2FM97Z2ZzfcQv8erIlryG9zm6Oo94Ug%2FsmDJIGIazzeG2ll9AQ%3D%3D', swid='{D24A8720-97F9-47EB-8A87-2097F987EBFA}')

tweet_data = "Big Baller League scores from Week 16\n \n"

for t in league.scoreboard(13):
    away_team = (str(t.away_team))
    home_team = (str(t.home_team))
    #print(away_team)
    #print(home_team)
 
    away_fix = team_to_nickname.get(away_team)
    home_fix = team_to_nickname.get(home_team)

    #print(away_fix)
    #print(home_fix)

    if t.away_score > t.home_score : 
        line = away_fix + " - " + str(t.away_score) + " --- " + str(t.home_score) + " - " + home_fix + "\n"
    else:
        line = home_fix + " - " + str(t.home_score) + " --- " + str(t.away_score) + " - " + away_fix + "\n"
 
    tweet_data += line

print(tweet_data)

api.update_status(status=tweet_data)
