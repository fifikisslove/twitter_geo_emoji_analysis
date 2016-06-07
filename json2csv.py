import json
import csv


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

city = "toulouse"
print("Starting post-processing into .csv for " + city)
get_data(city)
print("Finished. Data saved in " + city + ".csv")
