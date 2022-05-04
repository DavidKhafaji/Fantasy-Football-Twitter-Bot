# themodelbot

import tweepy as tp
import time
import os

# scraping libraries 
# beautiful soup aka bs4

# credentials to login to twitter api
#api_key = '2lSOCXCTXeLS9XxYDuxv18rWg'
#api_secret = 'HhjNRrDY7P0uK0IXkKcr8HllRdfIl60AW5bjq5hmHMrS541iM0'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKZTWQEAAAAApVoHlKBsPsbNbRe%2FTZM5E61Rnys%3DlH9VVfn6kSUkUmNEonZWlIU3uSRUeigQD7BzWvDBOpcXgKWlfV'
#access_token = '1465529313638424580-OjR9O5moJF4KgjhGALjYKiesE1sEkz'
#access_token_secret = 'AOioGS6quq2W90beV5IKBLMEcKD7WdETeGXX6kTeKZfuu'

# login to twitter account api
auth = tp.OAuthHandler("2lSOCXCTXeLS9XxYDuxv18rWg", "HhjNRrDY7P0uK0IXkKcr8HllRdfIl60AW5bjq5hmHMrS541iM0")
auth.set_access_token("1465529313638424580-dwXRXlfCXHtJArROhN8cuDhYsrvgqb", "ivlTivHl4ZcOvLXrdEpNa45YGfIFuvnQqxVGEUkltTUpF")
api = tp.API(auth)

#api.update_status_with_media("This Tweet was Tweeted using Tweepy!")


#os.chdir('models')

api.update_status(status="league.scoreboard")

#filename="./models/pexels-photo-982585.jpeg")
# iterates over pictures in models folder
#for model_image in os.listdir('.'):
#    #api.update_with_media(model_image)
#    api.update_status_with_media(status="hello", filename=model_image)
#    time.sleep(3)

#league.scoreboard

