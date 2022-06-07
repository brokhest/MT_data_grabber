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
