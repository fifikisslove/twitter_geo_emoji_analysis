
import json
import csv
import re


def get_data(city):
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
    with open("emoji.json", 'r') as f:
        emojies = json.load(f)
    try:
        tweet = json.loads(line)
    except ValueError:
        print("ValueError")

    emojies_list = list(emojies.keys())
    print("before")
    print(tweet['text'])
    new_tweet = ""
    for emoji in emojies_list:
        if emoji in tweet['text']:
            new_tweet += emoji
    date = tweet['created_at'].split(" ")
    return [new_tweet, date[0],date[3], tweet['user']['friends_count'], city]

city = "toulouse"
print("Starting post-processing into .csv for " + city)
get_data(city)
print("Finished. Data saved in emoji_data.csv")
