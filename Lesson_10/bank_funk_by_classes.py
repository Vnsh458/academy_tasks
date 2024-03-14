import json


class BankUser():
    def __init__(self, second_name, first_name, id) -> None:
        self.last_name = second_name
        self.first_name = first_name
        self.balance = 0
        self.credit = 0
        self.id = id + 1

    def create_user(self) -> None:
        with open('test_data_base.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            id = data["counts"]["count_action_users"] + 1

            data['users'][id] = {
                "last_name": self.second_name,
                "first_name": self.first_name,
                "balance": self.balance,
                "credit": self.credit,
                "id": self.id            
            }

            data["counts"]["count_action_users"] += 1
            data["transaction"][id] = []


        with open('test_data_base.json', 'w', encoding='utf-8') as update_file:
            json.dump(data, update_file)
        
        print("success")


    def change_user(id):
        with open('test_data_base.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)


        with open('test_data_base.json', 'w', encoding='utf-8') as update_file:
            json.dump(data, update_file)