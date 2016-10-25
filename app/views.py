from app import app, db
from .models import Item

from flask import render_template

from io import BytesIO
import bz2
import requests
import csv


@app.route('/hello')
def hello_world():
    return render_template('hello.html', name='Peter')
    # return 'hello world!'

# @app.route('/items')
# def items():


@app.route('/update')
def update():

    header_index = {
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

    # get the file from fuzzworks 
    response = requests.get('https://www.fuzzwork.co.uk/dump/latest/invTypes.csv.bz2')

    # unzip and parse the csv file
    spamreader = csv.reader(bz2.open(BytesIO(response.content), mode='rt'), delimiter=',')

    # delete all rows from the Item table
    # models.Item.query.delete()
    db.session.query(Item).delete()

    # loop over every row in the csv file
    for i, row in enumerate(spamreader):

        # skip the first row (it's column headers)
        if i == 0:
            continue

        # skip any rows that aren't marketable
        if row[header_index['marketGroupID']] == 'None':
            continue

        # store the row as an Item in the database
        db.session.add(Item(
            row[header_index['typeID']],
            row[header_index['groupID']],
            row[header_index['typeName']],
            (None if row[header_index['description']] == 'None' else row[header_index['description']]),
            (None if row[header_index['mass']] == 'None' else row[header_index['mass']]),
            (None if row[header_index['volume']] == 'None' else row[header_index['volume']]),
            (None if row[header_index['capacity']] == 'None' else row[header_index['capacity']]),
            (None if row[header_index['portionSize']] == 'None' else row[header_index['portionSize']]),
            (None if row[header_index['raceID']] == 'None' else row[header_index['raceID']]),
            (None if row[header_index['basePrice']] == 'None' else row[header_index['basePrice']]),
            (None if row[header_index['published']] == 'None' else row[header_index['published']]),
            (None if row[header_index['marketGroupID']] == 'None' else row[header_index['marketGroupID']]),
            (None if row[header_index['iconID']] == 'None' else row[header_index['iconID']]),
            (None if row[header_index['soundID']] == 'None' else row[header_index['soundID']]),
            (None if row[header_index['graphicID']] == 'None' else row[header_index['graphicID']]),
        ))

    # commit the changes to the database
    db.session.commit()

    return 'updated!'
