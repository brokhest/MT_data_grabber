

shipType_map = {
    #VTS - не интересует
    "0": "skip",
    "2": "fishing",
    # буксир
    "3": "tag",
    "6": "passenger",
    "7": "cargo",
    "8": "tanker",
    "9": "pleasure craft"
}

shipAttrs_map = {
    "LAT": "LATITUDE",
    "LON": 'LONGITUDE',
    # скорость поворота судна градус/минута
    "ROT": "ROTATION",
    # общая сумма переменных грузов судна в тоннах
    "DWT": "DEADWEIGHT",
    "SHIPNAME": 'NAME',
    "SHIP_ID": "ID",
    "SHIPTYPE": "type"

}