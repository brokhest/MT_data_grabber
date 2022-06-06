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
        return f"x:{self.__coords['x']}, y:{self.__coords['y']}, z:{self.__coords['x']}"

    def __repr__(self):
        return self.__coords

    def get(self):
        return self.__coords

    def start(self):
        self.__scan()

    def __scan(self):
        while self.__status:
            try:
                requests.get(url=self.__requests.page['url'], headers=self.__requests.page['headers'])
            except requests.exceptions.ConnectionError:
                print('faced connection error, will retry in 10 seconds')
                time.sleep(10)
                continue
            for i in range(12):
                for block in self.__test:
                    try:
                        data = requests.get(url=block['url'], headers=block['headers'])
                    except requests.exceptions.ConnectionError:
                        print('faced API connection error, will retry in 10 seconds')
                        time.sleep(10)
                        continue
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
        return ship_data

    def stop(self):
        self.__status = False
