

import json


def get_data():
    print("Starting")
    with open('emoji.json', 'r') as unicode_json:
        with open('emoji_cat.json', 'r') as category_json:
            category_data = json.load(category_json)
            unicode_data = json.load(unicode_json)
            for emoji in unicode_data:
                try:
                    put_together(emoji, unicode_data[emoji], category_data)
                except ValueError:
                    continue


def put_together(emoji, emoji_unicode, category_data):

    # emoji_unicode in format           U1F600
    # category_data[unicode] in format  1f600
    emoji_unicode = emoji_unicode[1:]
    # print emoji, emoji_unicode

    with open('processed_emoji.json', 'w') as processed_json:

        for key, value in category_data.iteritems():  # key is name, value is dict with information
            category_unicode = value["unicode"].upper()
            if category_unicode == emoji_unicode:

                print emoji, emoji_unicode, category_unicode, value["category"]

                result = {emoji: value["category"]}
                processed_json.write(json.dumps(result) + "\n")
                return

        processed_json.write(json.dumps({emoji: ""}) + "\n")


get_data()
