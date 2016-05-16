# twitter_geo_emoji_analysis

crawler.py
- crawl geolocalized tweet according to a list of cities we are interrested in
works alone, avoid twitter rate errors, store tweets from cities in different json file

data.txt
- contains the datas of the cities we are interrested in
paris lat,long,30km

emoji_analysis.py
- read tweets stored in json file
- return the following frequencies for each emoji in a dictionnary
- (number of time this_emoji appears/sum of emoji in the set)
- (number of time this_emoji appears/sum of tweets in the set)

emoji.json
- contains the list of twitter used emoji in unicode and hex format
