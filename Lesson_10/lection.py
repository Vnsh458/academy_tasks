import json


'''with open('data.json', 'r') as file:
    data = json.load(file)
    print(data['user']["first_name"])

    # load() -- принимает в себя файл, который считывает его и преобразовывает его в словарь

with open('data_new.json', 'w', encoding='utf-8') as file:
    data = {
        "Cars": {
            "Lada": 1000000,
            "BMW": 1700000,
        }
    }

    # dump() -- принимает в себя 2 аргумента. 1ый - словарь, преобразующийся в строку, 
    # а 2ой - это файл куда надо записать преобразованный словарь

    data = json.dump(data, file)

def update_json(mark, cost):
    with open('data_new.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)

        data['Cars'].update({mark: cost})

        # place the cursor at the beginning of the file
        file.seek(0)

        json.dump(data, file)
        file.truncate()

update_json(cost=60, mark="Ford")'''


