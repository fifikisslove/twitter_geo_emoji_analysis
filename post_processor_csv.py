# Takes data from crawler.py and puts it in database or just normal text document.

import json
import csv


def get_data(city):
    with open('emoji_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        with open(city + '.json', 'r') as f:
            for line in f:
                try:
                    processed_tweet = get_text(line, city)
                    csv_writer.writerow(processed_tweet)
                except ValueError:
                    continue


def get_text(tweet_json, city):
    try:
        json_data = json.loads(tweet_json)
    except ValueError:
        print "ValueError"

    result = dict()
    result['text'] = json_data['text']
    result['created_at'] = json_data['created_at']
    # result['coordinates'] = json_data['coordinates']
    result['friends_count'] = json_data['user']['friends_count']

    result = [json_data['text'], json_data['created_at'], json_data['user']['friends_count'], city]

    return result


# put in whatever city you need.
city = "zurich"
print "Starting post-processing into .csv for " + city
get_data(city)
print "Finished. Data saved in emoji_data.csv"
