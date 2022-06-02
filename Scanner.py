import time
from Requests import Requests
import requests
from Queue import Queue


class Scanner(object):

    def __init__(self, page, blocks):
        self.__status = True
        self.__requests = Requests(page, blocks)
        self.__coords = page
        self.__test = self.__requests.api
        # self.start()

    def __str__(self):
        return f"x:{self.__coords['x']}, y:{self.__coords['x']}, z:{self.__coords['x']}"

    def __repr__(self):
        return self.__coords

    def get(self):
        return self.__coords

    def start(self):
        self.__scan()

    def __scan(self):
        while self.__status:
            requests.get(url=self.__requests.page['url'], headers=self.__requests.page['headers'])
            # print(page.text)
            for block in self.__test:
                data = requests.get(url=block['url'], headers=block['headers'])
                useful_data = self.__convert(data.json())
                for ship in useful_data:
                    Queue.add(ship)
            time.sleep(10)

    @staticmethod
    def __convert(data):
        ship_data = []
        ships = data['data']
        for ship in ships['rows']:
            ship_data.append(ship)
        print(ships['areaShips'])
        return ship_data

    def stop(self):
        self.__status = False
