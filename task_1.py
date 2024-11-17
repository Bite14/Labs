import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    summa = sum([i.get('score') * i.get('weight') for i in data])

    return round(summa, 3)


print(task())