
import json
import csv
import re


def get_data(city):
    with open('test_emoji_data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        with open(city + '.json', 'r') as f:
            for line in f:
                try:
                    processed_tweet = get_text(line, city)
                    if processed_tweet != 0:
                        csv_writer.writerow(processed_tweet)
                except ValueError:
                    continue


def get_text(tweet_json, city):
    try:
        json_data = json.loads(tweet_json)
    except ValueError:
        print "ValueError"

    emojis = extract_emojis_regex(json_data['text'])
    if emojis:
        return [emojis, json_data['created_at'], json_data['user']['friends_count'], city]

    return 0


def extract_emojis_regex(text):
    '''emoji_list = re.findall(u'['
                      u'\U0001F300-\U0001F64F'
                      u'\U0001F680-\U0001F6FF'
                      u'\u2600-\u26FF\u2700-\u27BF]+',
                      text, re.UNICODE)
    '''

    emoji_list = re.findall(u'[\uD83D\uDE01-\uD83D\uDE4F]', text, re.UNICODE)

    emojis = ''.join(emoji_list)

    # emojis = shit.findall(text)
    # emojis = re.findall(ur'[\u1F601-\u1F64F]', text, re.UNICODE)
    if emojis:
        print emojis

    return emojis


# put in whatever city you need.
city = "zurich"
print "Starting post-processing into .csv for " + city
get_data(city)
print "Finished. Data saved in emoji_data.csv"
