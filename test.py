from Calculator import CoordinatesCalculator
from Logger import Logger
from multiprocessing import Process


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

    print(CoordinatesCalculator.calculate(area))
    Logger.clear()
    processes = []
    message = 'тестовое сообщение'
    for i in range (5):
        p = Process(target=Logger.log, args=[message])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
