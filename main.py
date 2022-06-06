import threading
import time
from DataGrabber import DataGrabber
from Calculator import CoordinatesCalculator
from multiprocessing import Process
from Queue import Queue
from Analyzer import Analyzer
from DBHook import DBHook
from analysis_controller import AnalysisController

if __name__ == "__main__":
    area = []
    top = {
        "x": {
            "degree": 131,
            "minute": 49,
            "second": 54
        },
        "y": {
            "degree": -43,
            "minute": 7,
            "second": 23
        }
    }
    area.append(top)
    bot = {
        "x": {
            "degree": 131,
            "minute": 57,
            "second": 30
        },
        "y": {
            "degree": -43,
            "minute": 2,
            "second": 57
        }
    }
    area.append(bot)
    location = CoordinatesCalculator.calculate(area)
    page = {
        "x": 131.872,
        "y": 43.133,
        "z": 12
    }
    blocks = []
    text = {
        "x": 1773,
        "y": 751,
        "z": 12
    }
    blocks.append(text)
    text = {
        "x": 1774,
        "y": 751,
        "z": 12
    }
    blocks.append(text)
    DataGrabber.start_scan(location['page'], location['blocks'])
    area = []
    top = {
        "x": {
            "degree": 117,
            "minute": 40,
            "second": 30
        },
        "y": {
            "degree": -39,
            "minute": 10,
            "second": 14
        }
    }
    area.append(top)
    bot = {
        "x": {
            "degree": 120,
            "minute": 18,
            "second": 21
        },
        "y": {
            "degree": -37,
            "minute": 48,
            "second": 12
        }
    }
    area.append(bot)
    coord = []
    a = {
        "x": {
            "degree": 131,
            "minute": 54,
            "second": 9.55
        }
    }
    location = CoordinatesCalculator.calculate(area)
    DataGrabber.start_scan(location['page'], location['blocks'])
    time.sleep(60)
    print("stopping")
    DataGrabber.stop_scan(0)
    time.sleep(60)
    print('stop')
    DataGrabber.stop_scan(0)
   #  AnalysisController.start()
   #  AnalysisController.notify()





