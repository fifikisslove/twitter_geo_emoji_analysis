"""
This algorithm extracts the main relevant data from tweet stored in json format and write it in a csv file.
It mainly focused on the emojies extraction which works with our emoji dataset.

GROUP 1, Social Media, TU Graz
15/05/215
"""

import json
import csv


def get_data(city):
    """
    :param city: the city we are currently analyzing.
    :return: write the data returned by the get_text function on a csv files which is more readable by our analysis tools.
    """
    print("a")
    with open(city + '.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        with open(city + '.json', 'r') as f:
            for line in f:
                try:
                    processed_tweet = get_text(line, city)
                    if processed_tweet != 0:
                        csv_writer.writerow(processed_tweet)
                except ValueError:
                    continue


def get_text(line, city):
    """
    :param line: correspond to all datas about one tweet.
    :param city: the city we are currently analyzing.
    :return: return a list of all datas we want to store in the csv file for analysis:
    the list of emojies in the tweets, the number of emojies per category (one column / categories,
    the total number of emojies in the tweet, the date, the day, the number of friends of the user and the city.
    """
    with open("processed_emoji.json", 'r') as f:
        emojies = json.load(f)
    try:
        tweet = json.loads(line)
    except ValueError:
        print("ValueError")

    emojies_list = list(emojies.keys())
    # print("before")
    # print(tweet['text'])
    new_tweet = ""
    number_of_emojis = 0  # number of emojis for this tweet
    categories = {'people': 0, 'nature': 0, 'activity': 0, 'food': 0, 'travel': 0, 'symbols': 0, 'objects': 0, 'flags': 0}  # people, nature, activity, food, travel, symbols, objects,

    for emoji in emojies_list:
        if emoji in tweet['text']:
            # print "emoji"
            new_tweet += emoji
            number_of_emojis += 1
            if emojies[emoji] in categories:
                categories[emojies[emoji]] += 1
    date = tweet['created_at'].split(" ")
    return [new_tweet, number_of_emojis, categories['people'], categories['nature'], categories['activity'],
            categories['food'], categories['symbols'], categories['objects'], categories['flags'],
            date[0], date[3], tweet['user']['friends_count'], city]

#city = ["graz","innsbruck","linz","milan","naples","rome","salzburg","vienna"]
#city = ["lyon","birmingham","leeds","london","marseille","paris"]
city = ["berlin_complete","hamburg_complete","krakow_complete","lodz_complete","munich_complete","warsaw_complete"]
for c in city:
    print("Starting post-processing into .csv for " + c)
    get_data(c)
    print("Finished. Data saved in " + c + ".csv")
