from datetime import datetime
import json


DATABASE = 'test_data_base.json'

def database_connect(database, mode, data=None):
    if mode.lower() == "w":
        with open(database, 'w', encoding='utf-8') as file:
            if data != None:
                return json.dump(data, file, indent=4, ensure_ascii=False)
    elif mode.lower() == 'r':
        with open(database, 'r', encoding='utf-8') as file:
            return json.load(file)


def create_user(first_name, second_name):    
    data = database_connect(database=DATABASE, mode='r')
    id = data["counts"]["count_action_users"] + 1

    data['users'][id] = {
        "last_name": second_name,
        "first_name": first_name,
        "balance": 0,
        "credit": 0,
        "id": id            
    }

    data["counts"]["count_action_users"] += 1
    data["transaction"][id] = {}


    data = database_connect(database=DATABASE, mode='w', data=data)
    
    return "User created successfully"

def change_user(id, **kwargs):
    data = database_connect(database=DATABASE, mode='r')

    for key, value in kwargs.items():
        data["users"][id][key] = value


    database_connect(database=DATABASE, mode='w', data=data)

def show_user(id):
    data = database_connect(database=DATABASE, mode='r')
    user = data['users'].get(id)

    if user:
        return user
    else:
        return "Такого пользователя нет"
    
def delete_user(id):    
    data = database_connect(database=DATABASE, mode='r')
    user = data['users'].get(id)

    if user:
        del data['users'][id]
        del data['transaction'][id]
    else:
        print("Такого пользователя нет")

    database_connect(database=DATABASE, mode='w', data=data)

def create_transaction(id, category, expense):
    data = database_connect(database=DATABASE, mode='r')

    data['transaction'][id]['time'] = str(datetime.now())
    data['transaction'][id]['category'] = category
    data['transaction'][id]['expense'] = expense

    database_connect(database=DATABASE, mode='w', data=data)
    
