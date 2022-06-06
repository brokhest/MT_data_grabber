from Calculator import CoordinatesCalculator


if __name__ == "__main__":
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

    print(CoordinatesCalculator.calculate(area))
