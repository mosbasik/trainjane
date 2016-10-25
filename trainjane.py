from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from io import BytesIO
import bz2
import requests
import csv

# set up our flask app
app = Flask(__name__)

# set some settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create our sqlalchemy connection to the db file
db = SQLAlchemy(app)

class Item(db.Model):
    typeID = db.Column(db.Integer, primary_key=True)
    groupID = db.Column(db.Integer)
    typeName = db.Column(db.String(150))
    description = db.Column(db.Text, nullable=True)
    mass = db.Column(db.Float, nullable=True)
    volume = db.Column(db.Float, nullable=True)
    capacity = db.Column(db.Float, nullable=True)
    portionSize = db.Column(db.Integer, nullable=True)
    raceID = db.Column(db.Integer, nullable=True)
    basePrice = db.Column(db.Float, nullable=True)
    published = db.Column(db.Boolean, nullable=True)
    marketGroupID = db.Column(db.Integer, nullable=True)
    iconID = db.Column(db.Integer, nullable=True)
    soundID = db.Column(db.Integer, nullable=True)
    graphicID = db.Column(db.Integer, nullable=True)
    
    def __init__(self, typeID, groupID, typeName, description, mass, volume, capacity, portionSize, raceID, basePrice, published, marketGroupID, iconID, soundID, graphicID):
        self.typeID = typeID
        self.groupID = groupID
        self.typeName = typeName
        self.description = description
        self.mass = mass
        self.volume = volume
        self.capacity = capacity
        self.portionSize = portionSize
        self.raceID = raceID
        self.basePrice = basePrice
        self.published = published
        self.marketGroupID = marketGroupID
        self.iconID = iconID
        self.soundID = soundID
        self.graphicID = graphicID

    def __repr__(self):
        return '<Item {} [{}]>'.format(self.typeName, self.typeID)


@app.route('/hello')
def hello_world():
    return 'hello world!'


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

    # loop over every row in the csv file
    for i, row in enumerate(spamreader):

        # skip the first row (it's just headers)
        if i == 0:
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
