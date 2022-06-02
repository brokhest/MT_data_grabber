import os
from sqlalchemy import create_engine, Column, INTEGER, REAL, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

engine = create_engine('sqlite:///relevant_data.db')
connection = engine.connect()


class Vessel(Base):
    __tablename__ = "vessels"
    id = Column(INTEGER, primary_key=True)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    speed = Column(INTEGER, nullable=False)
    course = Column(INTEGER, nullable=True)
    heading = Column(INTEGER, nullable=False)
    destination = Column(String(20), nullable=False)
    flag = Column(String(3), nullable=False)
    length = Column(INTEGER, nullable=False)
    width = Column(INTEGER, nullable=False)
    rotation = Column(INTEGER, nullable=False)
    name = Column(String(30), nullable=False)
    type = Column(String(20), nullable=False)
    deadweight = Column(INTEGER, nullable=False)


Base.metadata.create_all(engine)


class DBHook:

    @staticmethod
    def get(id):
        # if not DBHook.__exists():
        #     initialize()
        session = Session(bind=engine)
        ship = session.query(Vessel).get(id)
        session.close()
        if ship is not None:
            ship = DBHook.__convert_from_model(ship)
        return ship

    @staticmethod
    def add(ship):
        # if not DBHook.__exists():
        #     initialize()
        session = Session(bind=engine)
        ship = DBHook.__convert_to_model(ship)
        session.add(ship)
        session.commit()
        session.close()
        return

    @staticmethod
    def update(ship):
        session = Session(bind=engine)
        model = session.query(Vessel).get(ship['id'])
        DBHook.__update_model(ship, session)
        session.commit()
        session.close()
        return

    @staticmethod
    def __convert_to_model(ship):
        entry = Vessel(
            id=ship['id'],
            latitude=ship['latitude'],
            longitude=ship['longitude'],
            speed=ship['speed'],
            course=ship['course'],
            heading=ship['heading'],
            destination=ship['destination'],
            flag=ship['flag'],
            length=ship['length'],
            width=ship['width'],
            rotation=ship['rotation'],
            name=ship['name'],
            type=ship['type'],
            deadweight=ship['deadweight']
        )
        return entry

    @staticmethod
    def __convert_from_model(ship):
        entry = {
            "id": ship.id,
            "latitude": ship.latitude,
            "longitude": ship.longitude,
            "speed": ship.speed,
            "course": ship.course,
            "heading": ship.heading,
            "destination": ship.destination,
            "flag": ship.flag,
            "length": ship.length,
            "width": ship.width,
            "rotation": ship.rotation,
            "name": ship.name,
            "type": ship.type,
            "deadweight": ship.deadweight
        }
        return entry

    @staticmethod
    def __update_model(ship, model):
        model.latitude = ship['latitude'],
        model.longitude = ship['longitude'],
        model.speed = ship['speed'],
        model.course = ship['course'],
        model.heading = ship['heading'],
        model.destination = ship['destination'],
        model.flag = ship['flag'],
        model.length = ship['length'],
        model.width = ship['width'],
        model.rotation = ship['rotation'],
        model.name = ship['name'],
        model.type = ship['type'],
        model.deadweight = ship['deadweight']
        return model

    @staticmethod
    def __exists():
        return os.path.isfile(os.path.abspath("relevant_data.db"))


