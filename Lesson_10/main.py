from bank_functional import *


while True:

    print("-" * 20)
    print("Ваши возможности:")
    print("создать - создать нового пользователя")
    print("создать покупку - создать новую покупку")
    print("удалить - удалить пользователя")
    print("смотреть - просмотреть пользователя")
    print("выход - выходит из программы")
    print("-" * 20)

    command:str = input("Введите команду:\n")

    if command == "создать":
        print("-" * 20)
        first_name = input("Введите имя:\t")
        second_name = input("Введите фамилию:\t")

        create_user(first_name=first_name, second_name=second_name)

    elif command == "удалить":
        print("-" * 20)
        deleted_user = input("Введите ID пользователя, которого хотите удалить?\n")

        delete_user(deleted_user)

    elif command == "изменить":
        changed_user_id = input("Введите ID пользователя, которого хотите изменить?\n")
        while True:
            print("-" * 20)
            print("Что вы хотите изменить?")
            print("1 - Имя\n2 - Фамилию")
            print("3 - Баланс\n4 - Кредитную историю")
            print("5 - Все\n6 - Выход")
            change_command = input("Выберите что-нибудь:\n")

            if change_command == "1":
                new_name = input("Введите новое имя:\t")

                change_user(id=changed_user_id, first_name=new_name)

            elif change_command == "2":
                new_second_name = input("Введите новую фамилию:\t")

                change_user(id=changed_user_id, last_name=new_second_name)

            elif change_command == "3":
                new_balance = input("Введите новый баланс:\t")

                change_user(id=changed_user_id, balance=new_balance)

            elif change_command == "4":
                new_credit = input("Введите новую кредитную историю:\t")

                change_user(id=changed_user_id, credit=new_credit)
                
            elif change_command == "5":
                new_name = input("Введите новое имя:\t")
                new_second_name = input("Введите новую фамилию:\t")
                new_balance = input("Введите новый баланс:\t")
                new_credit = input("Введите новую кредитную историю:\t")

                change_user(id=changed_user_id, first_name=new_name, last_name=new_second_name, balance=new_balance, credit=new_credit)
            
            elif change_command == "6":
                break

    elif command == "смотреть":
        print("-" * 20)
        watched_user_id = input("Введите ID пользователя, которого хотите посмотреть?\n")

        print(show_user(watched_user_id))

    elif command == "создать покупку":
        transaction_id = input("Введите ID транзакции, которую вы хотите создать:\n")
        category = input("Введите категрию траты:\t")
        expense = input("Введите сумму:\t")

        create_transaction(id=transaction_id, category=category, expense=expense)

    elif command == "выход":
        break