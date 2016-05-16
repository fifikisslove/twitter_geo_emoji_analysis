"""
This algorithm analyze frequencies of occurence in already collected tweets.

GROUP 1, Social Media, TU Graz
15/05/215
"""


import json


# read our emojies : dict as
with open("emoji.json", 'r') as f:
    emojies = json.load(f)

# our readable emojies (encoding in the same way as in collected datas.
emojies_list = list(emojies.keys())


def get_emojies_from_specific_city(city):
    """
    # open a example file of tweet to be analyzed.
    # output is a list of dictionnaries
    # each case of the list is a dictionnary containing tweet data
    # the coordinates of the third tweet of the list can be access like that tweets[3]['coordinates']
    :return:
    """
    tweets = []
    with open(city + '.json', 'r') as f:
        for line in f:
            try:
                tweets.append(json.loads(line))
            except ValueError:
                continue
    return tweets


def get_emoji_frequencies(city):
    """
    :param city:
    :return: frequency dict
    """

    # initialisation of our frequencies dict
    frequencies = {}
    for emoji in emojies_list:
        frequencies[emoji] = 0

    # crawl of our datas
    tweets_of_this_city = get_emojies_from_specific_city(city)
    for tweet in tweets_of_this_city:
        for emoji in emojies_list:
            if emoji in tweet['text']:
                frequencies[emoji] +=1

    # transforming our current sum of emoji apparition into frequency
    sum = len(list(frequencies.values()))
    for key in frequencies:
        frequencies[key] /= sum

    return frequencies


# example with one city
print(get_emoji_frequencies('strasbourg'))



# create the result file if does not exist.
# overwritte if already exist.
# with open('results.json', 'w') as f:
