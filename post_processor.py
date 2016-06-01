# Takes data from crawler.py and puts it in database or just normal text document.

import re
import json


def get_data(city):
    with open(city + '_post.json', 'w') as f_processed:
        with open(city + '.json', 'r') as f:
            for line in f:
                try:
                    processed_tweet = get_text(line)
                    f_processed.write(json.dumps(processed_tweet) + "\n")
                except ValueError:
                    continue


def get_text(tweet_json):
    try:
        json_data = json.loads(tweet_json)
    except ValueError:
        print "ValueError"

    result = dict()
    result['text'] = json_data['text']
    result['created_at'] = json_data['created_at']
    # result['coordinates'] = json_data['coordinates']
    result['friends_count'] = json_data['user']['friends_count']

    return result


# put in whatever city you need.
city = "zurich"
print "Starting post-processing for " + city
get_data(city)
