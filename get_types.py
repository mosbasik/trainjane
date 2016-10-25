from io import BytesIO
import bz2
import requests
import csv

from enum import Enum

indexes = {
    'typeID': 0,
    'groupID': 1,
    'typeName': 2,
    'description': 3,
    'mass': 4,
    'volume': 5,
    'capacity': 6,
    'portionSize': 7,
    'raceID': 8,
    'basePrice': 9,
    'published': 10,
    'marketGroupID': 11,
    'iconID': 12,
    'soundID': 13,
    'graphicID': 14,
}

items = []

response = requests.get('https://www.fuzzwork.co.uk/dump/latest/invTypes.csv.bz2')
spamreader = csv.reader(bz2.open(BytesIO(response.content), mode='rt'), delimiter=',')
for row in spamreader:
    # print(', '.join(row))
    items.append(row[indexes['typeName']])


used = []
unique = [x for x in items if x not in used and (used.append(x) or True)]
print(', '.join(unique))

longest = max(items, key=len)
print('[{}] {}'.format(len(longest), longest))



# with open('invTypes.csv', 'wb') as csvfile:
# print(type(response.content))

