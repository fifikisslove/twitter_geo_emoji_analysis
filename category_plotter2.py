import csv
from matplotlib.pylab import plt
from prettytable import PrettyTable
import numpy as np


def calculate_percentage(city):
    """
    Calculates and adds normalized data to the data dictionary.

    Format:
    key: city name (e.g. zurich, munich, london
    value: array with category values (e.g [0.5, 0.1, 0.1, 0.1,....])
    """

    categories_count = [0]*8
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


def rearrange_data():

    # new_data = {'people': [], 'nature': [], 'activity': [], 'food': [], 'symbols': [], 'objects': [],
    #            'flags': [], 'uncategorized': []}
    new_data = [[0 for x in range(26)] for y in range(8)]

    
    #for city, array in data:
    for city in data.keys():
        i = cities.index(city)
        for j in range(8):
            new_data[j][i] = data[cities[i]][j]

    print 'SUM', sum(row[0] for row in new_data)


    p = PrettyTable(["City name","people","nature","activity","food","symbols","objects","flags","uncategorized"])
   
    for city, array in data.items():
        p.add_row([city, array[0],array[1],array[2],array[3],array[4],array[5],array[6], array[7]])

    #Nice tables
    print p.get_string(fields=["City name", "people", "nature", "food"])
    print p.get_string(fields=["City name", "people", "nature", "food"], start = 0, end = 1)

    
    return new_data


def plot():
    plt.figure(figsize=(20, 10))
    width = 0.5
    index = np.arange(26)

    print 'SUM PLOT 1', sum(row[0] for row in data)
    print 'SUM PLOT 2', sum(row[1] for row in data)
    print 'SUM PLOT 3', sum(row[2] for row in data)

    print data[0]
    
    p0 = plt.bar(index, data[0], width, color='y')  # people
    p1 = plt.bar(index, data[1], width, color='g')  # nature
    p2 = plt.bar(index, data[2], width, color='r')  # activity
    p3 = plt.bar(index, data[3], width, color='b')  # food
    p4 = plt.bar(index, data[4], width, color='c')  # symbols
    p5 = plt.bar(index, data[5], width, color='m')  # objects
    p6 = plt.bar(index, data[6], width, color='k')  # flags
    p7 = plt.bar(index, data[7], width, color='w')  # uncategorized


    plt.ylabel('Usage')
    plt.title('Emoji category usage per city')
    plt.xticks(index + width/2.0, cities)
    plt.yticks(np.arange(0, 1, 0.1))
    plt.legend((p0[0], p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0]), categories_names)

    plt.show()
    # plt.savefig("emoji_categories_cities.png")


def calc_all():

    for city in cities:
        calculate_percentage(city)
        # print data


cities = ["barcelona", "basel", "berlin", "birmingham", "geneva", "graz", "hamburg", "innsbruck", "krakow", "leeds",
          "linz", "lodz", "london", "lyon", "madrid", "marseille", "milan", "munich", "naples", "paris", "rome",
          "salzburg", "seville", "vienna", "warsaw", "zurich"]
categories_names = ['people', 'nature', 'activity', 'food', 'symbols', 'objects', 'flags', 'uncategorized']

data = {}
print "Starting calculations."
calc_all()
print "Finished with calculations."
data = rearrange_data()
plot()

