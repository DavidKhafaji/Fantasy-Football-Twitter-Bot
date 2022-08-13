import tweepy as tp
import requests
from bs4 import BeautifulSoup as bs
import os
from espn_api.football import League

team_to_nickname = {
    "Team(Zekes Meat)" : "Faji",
    "Team(Juan Carlos Fan Club)" : "Nick",
    "Team(Chacal De La Trompeta)" : "John",
    "Team(Hasbulla Hive)" : "CJ",
    "Team(# NewUs)" : "David",
    "Team(4KT Baby)" : "Edson",
    "Team(Loading Loading)" : "Nate",
    "Team(2 Girls 1 Kupp)" : "Alex",
    "Team(CMC IS FRAUDULENT)" : "Matt",
    "Team(O.J.'s Parole Board)" : "Brendan",
    "Team(Yup  In my white Tee)" : "Micah",
    "Team(Chase My BQNE)" : "Tyler"
}


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKZTWQEAAAAApVoHlKBsPsbNbRe%2FTZM5E61Rnys%3DlH9VVfn6kSUkUmNEonZWlIU3uSRUeigQD7BzWvDBOpcXgKWlfV'
auth = tp.OAuthHandler("2lSOCXCTXeLS9XxYDuxv18rWg", "HhjNRrDY7P0uK0IXkKcr8HllRdfIl60AW5bjq5hmHMrS541iM0")
auth.set_access_token("1465529313638424580-dwXRXlfCXHtJArROhN8cuDhYsrvgqb", "ivlTivHl4ZcOvLXrdEpNa45YGfIFuvnQqxVGEUkltTUpF")
api = tp.API(auth)

league = League(league_id=204259, year=2022, espn_s2='AEA70mrmO016Z0%2F58d01ogYZQqTQlO3NlY8Yn9dmi0YJaIxUSwHRu1PlPJ2b3dDelSyAbHTsnLcdv3vZzX%2BHceMa70DLsKc2uxbkhDa0gUObZ%2Bo6%2FKXYWU8CXK8TcF3hWczViNxPV3WLpkCIL71KrSKAdOOeUkLe123Y1uB0XWtBgSH5Pao9wakB%2FHEyCk8tJowksVdlXMYhC7W%2B7TY1C5PJAQiPPtrSkhizhu%2BEuP8%2Bu6yYEhaEpkBDdCQGvfp2OrBiXC4VqoyvBktjMORaHNM11M8yoTKlMXzY3HqbhdkS%2FQ%3D%3D', swid='{D24A8720-97F9-47EB-8A87-2097F987EBFA}')

tweet_data = "Big Baller League scores from Week 1\n \n"

for t in league.scoreboard(1):
    away_team = (str(t.away_team))
    home_team = (str(t.home_team))
 
    away_fix = team_to_nickname.get(away_team)
    home_fix = team_to_nickname.get(home_team)

    print(away_fix)
    print(home_fix)

    if t.away_score > t.home_score : 
        line = away_fix + " - " + str(t.away_score) + " --- " + str(t.home_score) + " - " + home_fix + "\n"
    else:
        line = home_fix + " - " + str(t.home_score) + " --- " + str(t.away_score) + " - " + away_fix + "\n"
 
    tweet_data += line

print(tweet_data)

api.update_status(status=tweet_data)



#team_to_nickname = {
  #"Faji": "Team(Zekes Meat)",
  #"Nick": "Team(Juan Carlos Fan Club)",
  #"John": "Team(Chacal De La Trompeta)",
  #"CJ":   "Team(Hasbulla Hive)",
  #"David": "Team(# NewUs)",
  #"Edson": "Team(4KT Baby)",
  #"Nate": "Team(Loading Loading)",
  #"Alex": "Team(2 Girls 1 Kupp)",
  #"Matt": "Team(CMC IS FRAUDULENT)",
  #"Brendan": "Team(O.J.'s Parole Board)",
  #"Micah": "Team(Yup  In my white Tee)",
  #"Tyler": "Team(Chase My BQNE)"

  #team_to_nickname = {
    #"Team(Zekes Meat)" : "Faji",
    #"Team(Juan Carlos Fan Club)" : "Nick",
    #"Team(Chubb  Crunch)" : "John",
    #"Team(Hasbulla Hive)" : "CJ",
   # "Team(Tannehill  Hive)" : "David",
   # "Team(#WolfTeam .)" : "Edson",
    #"Team(Unsolicited Dak Pics)" : "Nate",
    #"Team(2 Girls 1 Kupp)" : "Alex",
   # "Team(CMC IS FRAUDULENT)" : "Matt",
    #"Team(O.J.'s Parole Board)" : "Brendan",
    #"Team(Yup  In my white Tee)" : "Micah",
    #"Team(Mr.  Unlimited)" : "Tyler"
#}

  #EC2 AEA70mrmO016Z0%2F58d01ogYZQqTQlO3NlY8Yn9dmi0YJaIxUSwHRu1PlPJ2b3dDelSyAbHTsnLcdv3vZzX%2BHceMa70DLsKc2uxbkhDa0gUObZ%2Bo6%2FKXYWU8CXK8TcF3hWczViNxPV3WLpkCIL71KrSKAdOOeUkLe123Y1uB0XWtBgSH5Pao9wakB%2FHEyCk8tJowksVdlXMYhC7W%2B7TY1C5PJAQiPPtrSkhizhu%2BEuP8%2Bu6yYEhaEpkBDdCQGvfp2OrBiXC4VqoyvBktjMORaHNM11M8yoTKlMXzY3HqbhdkS%2FQ%3D%3D
  #swid {D24A8720-97F9-47EB-8A87-2097F987EBFA}

  #EC2 2021 AECIEghq5X3%2FU3I6LcjMyd%2FX2YWPqMnIV5KWswQx4cFvDUhSNxq3ZGRRc%2F9TZAhCR9LmoNlBG2TVs%2Bks3cIS33l7OKGMk48HDwE7IUrJTGQlk5kFirzy5mEP7ivJHv1NdmDHw3STSSdPxcQ9fmLtq1jBvFXizrmLpYNJvl5NpLbMwkdYwfIg5O9jHiOtTdf1EIl6A8m7oBNHFU5tuQ8bflIPzfcrZmfCQD9Ma2jp58bDAn%2BuD787Y2CIkJu7hLsjKLucCELayM6UCtS5bK8%2BwkqECvZinxGlrE5O%2FVBHCwnhZeQp5biy8uJ4Ho3YPt74LGs%3D', swid='{D24A8720-97F9-47EB-8A87-2097F987EBFA}