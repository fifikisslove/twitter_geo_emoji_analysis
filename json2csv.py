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
    with open("emoji.json", 'r') as f:
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
    categories = list()  # all categories of emojis for this tweet

    for emoji in emojies_list:
        if emoji in tweet['text']:
            # print "emoji"
            new_tweet += emoji
            number_of_emojis += 1
            if emojies[emoji] is not None:
                categories.append(emojies[emoji])
    date = tweet['created_at'].split(" ")
    return [new_tweet, number_of_emojis, " ".join(categories), date[0], date[3], tweet['user']['friends_count'], city]

city = "zurich"
print("Starting post-processing into .csv for " + city)
get_data(city)
print("Finished. Data saved in " + city + ".csv")
