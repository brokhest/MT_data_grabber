import threading
import time
from DataGrabber import DataGrabber
from Calculator import CoordinatesCalculator


if __name__ == "__main__":
    area = []
    top = {
        "x": {
            "degree": 131,
            "minute": 49,
            "second": 54
        },
        "y": {
            "degree": 43,
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
            "degree": 43,
            "minute": 2,
            "second": 57
        }
    }
    area.append(bot)
    #location = CoordinatesCalculator.calculate(area)
    print(CoordinatesCalculator.calculate(area))
    #DataGrabber.start_scan(area)
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
    print(CoordinatesCalculator.calculate(area))
    #location = CoordinatesCalculator.calculate(area)
    #DataGrabber.start_scan(area)
    # DataGrabber.start_scan(location['page'], location['blocks'])
    #time.sleep(60)
    print("stopping")
    #DataGrabber.stop_scan(0)
    #time.sleep(60)
    print('stop')
    #DataGrabber.stop_scan(0)

    area = []
    top = {
        "x": {
            "degree": -117,
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
            "degree": -120,
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
    #DataGrabber.start_scan(area)
    #time.sleep(10)
    #DataGrabber.stop_scan(0)





