import Analysis_controller
import DataGrabber
from Calculator import CoordinatesCalculator
from Logger import Logger
from multiprocessing import Process
from Request import Request


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
            "second": 23,
            'hemisphere': 'n'
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
            "second": 57,
            'hemisphere': 'n'
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

    #print(CoordinatesCalculator.calculate(area))
    #loc = CoordinatesCalculator.calculate(area)
    #req = Request(loc['page'], loc['blocks'])
    #Logger.clear()
    #processes = []
    #message = 'тестовое сообщение'
    mutex = DataGrabber.DataGrabber.get_mutex()
    Analysis_controller.AnalysisController.start(mutex)

