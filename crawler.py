"""
This algorithm collects tweets from various given areas.
It avoids rate limit errors from twitter REST API.

GROUP 1, Social Media, TU Graz
15/05/215
"""

from tweepy import OAuthHandler
import tweepy
import json
import time
import os


#Twitter API keys/tokens
consumer_key = 'RmyY6ECiWiD3IdFMQZsHJQbNM'
consumer_secret = 'aTwCNvzLYYxsJ6PMZDQFKClejBiu8QPrQaNizMshTN47vGIA1K'
access_token = '730081635530616836-bLPBxgSVk2NwTtZulJqykKzk9QJnpix'
access_secret = 'tFe8H4kBsjk0x0cZjHDvDbN7Tx61Asp3IJ1wwtlBGivpj'


#Authentification
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def limit_handled(cursor):
    """
    this function avoid rate limit errors from twitter REST API.
    """
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def collect_tweets(city, geocode, date1, date2, query="*"):
    """
    geocode : current used geocode.
    query is a filter for tweet collecting. By default "*" means no filter used.
    :return: nothing.
    """
    cursor = (tweepy.Cursor(api.search, q=query, geocode=geocode, since=date1, until=date2,).items())
    print('start')
    print(cursor.__sizeof__())
    with open(city + date1 + '.json', 'a') as f:
        for tweet in cursor:
            print(tweet.created_at)
            f.write(json.dumps(tweet._json))
            f.write("\n")
    print("TWEETS COLLECTION FROM" + city + "FINISHED")



def reading_cities():
    """
    read data from the .txt files containing each city we are interested in and its geolocalization.
    :return: Dictionary as {"Paris":"12.8742, 34.54099, 100km", "Paris":"12.8742, 34.54099, 100km"}
    """
    cities = {}
    for city in open('data.txt','r'):
        cities[city.split(' ')[0]] = city.split(' ')[1]
    return cities

def reading_date():
    """
    read data from the .txt files containing each date we are interested in.
    :return: list of dates
    """
    dates = []
    for date in open('data.txt','r'):
        dates.append(date)
    return cities


def load_balancer():
    """
    print some stats for the user (always cool to print some output, it looks more professional).
    default is "paris" (mostly for the first iteration)
    :return: the next city to analyze.
    """
    next_city = "paris"
    min = 1000000000000
    for file in os.listdir():
        if '.json' in file:
            n = sum(1 for line in open(file))
            print("{} TWEETS FROM {} ".format(n, file))
            if(n < min):
                min = n
                next_city = file.split('2')[0]
    return next_city


def initialize(cities, date1):
    """
    if does not exist, create the json file from each city.
    :param cities: cities in which we are interested in.
    :return:
    """
    print('lol')
    our_current_files = os.listdir()
    for name in cities:
        print('loll')
        file = name + date1 + ".json"
        if file in our_current_files:
            print("{}{}.json already exists".format(name,date1))
        else:
            open(name + date1 + '.json', 'a')



if __name__ == '__main__':

    date1="2016-05-23"
    date2="2016-05-24"

    initialize((reading_cities()), date1)
    cities = reading_cities()
    while True:
        next_city = load_balancer()
        try:
            collect_tweets(next_city, cities[next_city], date1, date2)
        except tweepy.TweepError:
            print("Rate limit reached, waiting 15 minutes.")
            time.sleep(15 * 60)
