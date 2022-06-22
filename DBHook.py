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
    heading = Column(INTEGER, nullable=True)
    destination = Column(String(20), nullable=True)
    flag = Column(String(3), nullable=False)
    length = Column(INTEGER, nullable=False)
    width = Column(INTEGER, nullable=False)
    rotation = Column(INTEGER, nullable=True)
    name = Column(String(30), nullable=False)
    type = Column(String(20), nullable=False)
    deadweight = Column(INTEGER, nullable=True)


class SATAIS(Base):
    __tablename__ = "SAT AIS"
    id = Column(String(70), primary_key=True)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    speed = Column(INTEGER, nullable=True)
    course = Column(INTEGER, nullable=True)
    heading = Column(INTEGER, nullable=True)
    type = Column(String(20), nullable=False)


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
    def get_ais(id):
        session = Session(bind=engine)
        ship = session.query(SATAIS).get(id)
        session.close()
        if ship is not None:
            ship = DBHook.__convert_from_model_ais(ship)
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
    def add_ais(ship):
        session = Session(bind=engine)
        ship = DBHook.__convert_to_model_ais(ship)
        session.add(ship)
        session.commit()
        session.close()
        return

    @staticmethod
    def update(ship):
        session = Session(bind=engine)
        model = session.query(Vessel).get(ship['id'])
        DBHook.__update_model(ship, model)
        session.commit()
        session.close()
        return

    @staticmethod
    def update_ais(ship):
        session = Session(bind=engine)
        model = session.query(SATAIS).get(ship['id'])
        DBHook.__update_model(ship, model)
        session.commit()
        session.close()

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
    def __convert_to_model_ais(ship):
        entry = SATAIS(
            id=ship['id'],
            latitude=ship['latitude'],
            longitude=ship['longitude'],
            speed=ship['speed'],
            course=ship['course'],
            heading=ship['heading'],
            type=ship['type']
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
    def __convert_from_model_ais(ship):
        entry = {
            "id": ship.id,
            "latitude": ship.latitude,
            "longitude": ship.longitude,
            "speed": ship.speed,
            "course": ship.course,
            "heading": ship.heading,
            "type": ship.type,
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
        model.rotation = ship['rotation'],
        model.deadweight = ship['deadweight']
        return model

    @staticmethod
    def __update_model_ais(ship, model):
        model.latitude = ship['latitude'],
        model.longitude = ship['longitude'],
        model.speed = ship['speed'],
        model.course = ship['course'],
        model.heading = ship['heading'],
        return model

    @staticmethod
    def __exists():
        return os.path.isfile(os.path.abspath("relevant_data.db"))
