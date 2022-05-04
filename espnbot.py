# model scraping for themodelbot
import requests
from bs4 import BeautifulSoup as bs
import os
from espn_api.football import League

league = League(league_id=204259, year=2021, espn_s2='AECIEghq5X3%2FU3I6LcjMyd%2FX2YWPqMnIV5KWswQx4cFvDUhSNxq3ZGRRc%2F9TZAhCR9LmoNlBG2TVs%2Bks3cIS33l7OKGMk48HDwE7IUrJTGQlk5kFirzy5mEP7ivJHv1NdmDHw3STSSdPxcQ9fmLtq1jBvFXizrmLpYNJvl5NpLbMwkdYwfIg5O9jHiOtTdf1EIl6A8m7oBNHFU5tuQ8bflIPzfcrZmfCQD9Ma2jp58bDAn%2BuD787Y2CIkJu7hLsjKLucCELayM6UCtS5bK8%2BwkqECvZinxGlrE5O%2FVBHCwnhZeQp5biy8uJ4Ho3YPt74LGs%3D', swid='{D24A8720-97F9-47EB-8A87-2097F987EBFA}')

print(league.scoreboard())

for t in league.scoreboard(1):
    print(str(t.away_team) + " - " + str(t.away_score) + " --- " + str(t.home_score))

#league.matchup

# get to fantasy login
#fantasyLogin = 'https://registerdisney.go.com/jgc/v6/client/ESPN-ONESITE.WEB-PROD/guest/login?langPref=en-US'

#client = requests.Session()


#html = client.get("https://espn.com").content
#soup = bs(html, "html.parser")
#csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')


#print(client.get("https://fantasy.espn.com/football/boxscore?leagueId=1989688176&matchupPeriodId=13&seasonId=2021&teamId=2").text)


#testPage = requests.get(fantasyLogin)
#print(testPage)
# enter my username and password & submit login

# am i logged in

#resultsPage = requests.get("https://fantasy.espn.com/football/team?leagueId=204259&teamId=7&seasonId=2021&scoringPeriodId=11&statSplit=singleScoringPeriod")

# download page for parsing
#page = requests.get(url)
#soup = bs(page.text, 'html.parser')

#print(soup)

# locate all elements with image tag
#image_tags = soup.findAll('img')

#print(image_tags)

# create directory for model images
#if not os.path.exists('models'):
#    os.makedirs('models')

# move to new directory
#os.chdir('models')






