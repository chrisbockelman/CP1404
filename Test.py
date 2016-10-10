# with open('items.csv') as file:
#     for line in file:
#         line_str = line.strip()
#         print(line_str)
from operator import itemgetter
def display_list(r):
    #items = []
    #totalPrice = []
    with open('items.csv') as file:
        count = 1
        for line in file:
            line_str = line.strip()
            # item, price, priority, tag = line_str.split(',')
            print(line_str)
            # print("{}. {:20} ${:>6.2f} ({})".format(count, item.capitalize(), price, priority))
        #     items.append([item,float(price),int(priority),tag])
        #     totalPrice.append(float(price))
        # items.sort(key=itemgetter(0, 2))
        # for item in items:
        #     if item[3] == menuChoice:
        #         print("{}. {:20} ${:>6.2f} ({})".format(count, item[0].capitalize(), item[1], item[2]))
        #         count += 1
