import csv
from matplotlib.pylab import plt


def calculate_percentage(city):
    """
    Calculates and adds normalized data to the data dictionary.

    Format:
    key: city name (e.g. zurich, munich, london
    value: array with category values (e.g [0.5, 0.1, 0.1, 0.1,....])
    """

    categories_count = [0]*8
    # categories_names = ['people', 'nature', 'activity', 'food', 'symbols', 'objects', 'flags', 'uncategorized']
    total = 0

    with open(city + "2.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            emojis_exist = row[1] != '0'
            not_first_row = row[0] != 'Tweet'

            if emojis_exist and not_first_row:
                row_total = int(row[1])
                total += row_total
                category_sum = 0

                for i in range(7):
                    category_count = int(row[2 + i])
                    categories_count[i] += category_count
                    category_sum += category_count

                categories_count[7] += row_total - category_sum

        normalized_category_count = []
        for category in categories_count:
            normalized_category_count.append(1.0 * category / total)

        data[city] = normalized_category_count


def plot(ranks):
    plt.figure(figsize=(20, 10))

    for row in range(0, 20):
        s = row / 20.0
        plt.plot(ranks[row], label='s = ' + str(s))

    plt.title("Emoji category usage by city")
    plt.ylabel("Category usage")
    plt.xlabel("Cities")
    # plt.legend(loc=9, ncol=5)
    plt.savefig("emoji_categories_cities.png")


def calc_all():

    cities = ["barcelona", "basel", "berlin", "birmingham", "geneva", "graz", "hamburg", "innsbruck", "krakow", "leeds",
              "linz", "lodz", "london", "lyon", "madrid", "marseille", "milan", "munich", "naples", "paris", "rome",
              "salzburg", "seville", "vienna", "warsaw", "zurich"]
    for city in cities:
        calculate_percentage(city)
        print data


data= {}
print "Starting calculations."
calc_all()
print "Finished with calculations."

