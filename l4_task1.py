import json

INPUT_FILENAME = 'input.json'


# TODO решите задачу
def task() -> float:
    with open(INPUT_FILENAME) as file:
        data = json.load(file)
    result = round(sum(dict_['score'] * dict_['weight'] for dict_ in data), 3)
    return float(result)


print(task())
