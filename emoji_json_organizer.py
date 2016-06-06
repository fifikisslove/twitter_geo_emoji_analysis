import json


def get_data():
    result = {}
    print("Starting")
    with open('emoji.json', 'r') as unicode_json:
        with open('emoji_cat.json', 'r') as category_json:
            category_data = json.load(category_json)
            unicode_data = json.load(unicode_json)
            for emoji in unicode_data:
                try:
                    cat = put_together(emoji, unicode_data[emoji], category_data)
                    result[emoji] = cat
                except ValueError:
                    continue
    with open('processed_emoji.json', 'w') as processed_json:
        processed_json.write(json.dumps(result))


def put_together(emoji, emoji_unicode, category_data):

    # emoji_unicode in format           U1F600
    # category_data[unicode] in format  1f600
    emoji_unicode = emoji_unicode[1:]
    if len(emoji_unicode) > 6:
        emoji_unicode = emoji_unicode[:5] + emoji_unicode[-5:]
        print emoji_unicode,
    # print emoji, emoji_unicode

    with open('processed_emoji.json', 'w') as processed_json:

        for key in category_data:  # key is name, value is dict with information
            category_unicode = category_data[key]["unicode"]
            if len(category_unicode) > 6:
                category_unicode = category_unicode[:5] + category_unicode[-5:]
                print category_unicode
            if category_unicode.upper() == emoji_unicode:
                result = {emoji: category_data[key]["category"]}
                return category_data[key]["category"]

        processed_json.write(json.dumps({emoji: ""}) + "\n")


get_data()
