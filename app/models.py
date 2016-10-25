from app import db

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
