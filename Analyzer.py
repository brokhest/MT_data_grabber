import time

from Queue import Queue
from ShipMap import shipType_map, shipAttrs_map
from DBHook import DBHook


class Analyzer(object):

    def __init__(self):
        self.__status = True

    def start(self):
        self.__analyze()

    def stop(self):
        self.__status = False

    def __analyze(self):
        num = 0
        while self.__status:
            ship = self.__grab()
            if ship is None:
                continue
            num += 1
            if ship is None:
                continue
            ship = self.__refine(ship)
            if not self.__validate(ship):
                continue
            relevance = self.__is_relevant(ship)
            if relevance == 0:
                DBHook.add(ship)
                # print('record: ' + str(num))
            elif relevance == 1:
                DBHook.update(ship)
                # print('record: ' + str(num))

    @staticmethod
    def __grab():
        if Queue.is_empty():
            time.sleep(10)
            print('Проснулся')
            return None
        ship = Queue.take()
        return ship

    @staticmethod
    def __refine(ship):
        if 'ELAPSED' in ship:
            ship.pop("ELAPSED")
        if "L_FORE" in ship:
            ship.pop("L_FORE")
        if 'W_LEFT' in ship:
            ship.pop("W_LEFT")
        if "GT_SHIPTYPE" in ship:
            ship.pop("GT_SHIPTYPE")
        ship = {shipAttrs_map[k].lower() if k in shipAttrs_map else k.lower(): v for k, v in ship.items()}
        if ship['type'] in shipType_map:
            ship.update({'type': shipType_map[ship['type']]})
        else:
            print('\nНОВЫЙ ТИП:')
            print(ship)
            ship.update({'type': "new"})
        return ship

    @staticmethod
    def __validate(ship):
        integrity = True
        if not all(key in ship for key in ('latitude',
                                           'longitude',
                                           'speed',
                                           'course',
                                           'heading',
                                           'destination',
                                           'flag',
                                           'length',
                                           'name',
                                           'type',
                                           'id',
                                           'width',
                                           'deadweight',
                                           'rotation')):
            integrity = False
        for k, v in ship.items():
            if v is None:
                integrity = False
                break
        if ship['type'] == "skip":
            integrity = False
        return integrity

    @staticmethod
    def __is_relevant(ship):
        # 0 - записи нет
        # 1 - обновить запись
        # 2 - неактульно
        record = DBHook.get(ship['id'])
        if record is None:
            return 0
        elif not ship == record:
            # print('new data')
            # print(ship)
            # print('old data')
            # print(record)
            return 1
        else:
            return 2
