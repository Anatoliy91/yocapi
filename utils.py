import json


# этот метод парсит Джейсон и возвращает дикт
def default_json_to_dict(json_data):
    dict_data = json.loads(json_data)
    return dict_data


# этот метод превращает дикт в Джейсон. Возвращает джейсон
def default_dict_to_json(diction):
    jsondata = json.dumps(diction)
    return jsondata

