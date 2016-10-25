from io import BytesIO
import bz2
import requests
import csv

response = requests.get('https://www.fuzzwork.co.uk/dump/latest/invTypes.csv.bz2')

# csvfile = bz2.decompress(response.content)

# with bz2.open(BytesIO(response.content), mode='rt') as csvfile:

#     for line in csvfile:
#       print(line)

    # spamreader = csv.reader(csvfile, delimiter=',')
    # for row in spamreader:
    #     print(', ').join(row)

spamreader = csv.reader(bz2.open(BytesIO(response.content), mode='rt'), delimiter=',')
# for row in spamreader:
#     print(', '.join(row))



# with open('invTypes.csv', 'wb') as csvfile:
# print(type(response.content))

