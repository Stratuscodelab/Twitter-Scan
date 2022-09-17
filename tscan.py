

import twint
import pyfiglet
#This module exports the JSON into stdout
import sys
import json

#The banner for the application
ascii_banner = pyfiglet.figlet_format("Twitter Scan")
print(ascii_banner)


search =  input("What are you searching for? ")
city = input("Where? ")
#user = input("user")


c = twint.Config()

c.Search = search
c.Near = city
c.Limit = 20
c.Popular_tweets = True
c.Store_json = True
c.Output = "tweets.json"

twint.run.Search(c)
