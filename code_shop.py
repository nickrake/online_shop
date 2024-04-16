from sql_scripts import ShopDB
import sqlite3

db = ShopDB("shop.db")

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()


def search_game():
    print("Введіть назву відео гри")
    game_title = input(":").lower()
    if db.search_email(game_title):
        for row in db.search_email(game_title):
            quantity, title, price, description, category, developer, platform = row
            print("Назва гри:", title, "\n")
            print("Ціна:", price, "\n")
            print("Розробник:", developer, "\n")
            print("Жанр:", category, "\n")
            print("Опис:", description, "\n")
            print("Платформа:", platform, "\n")
            print("Кількість на складі:", quantity, "\n")

    else:
        print("Відео гра з такою назвою не знайдена", "\n")


def create_account():
    print("Введіть своє імя")
    name = input(":")

    print("Введіть свою фамілію")
    surname = input(":")

    print("Введіть свій пароль")
    password = input(":")

    while True:
        print("Введіть свій емейл")
        email = input(":")
        if db.is_email_exist(email):
            print("Аккаунт з таким емейлом вже існує", "\n")
        else:
            break

    while True:
        print("Введіть свій номер телефону")
        phone = input(":")

        if db.is_phone_exist(phone):
            print("Аккаунт з таким номером телефону вже існує", "\n")
        else:
            break

    while True:
        print("Чи ви хочете ввести місто? (не обовязково)", "\n")
        print("y - так")
        print("n - ні")
        q = input(":")
        if q == "y":
            print("Введіть своє місто")
            city = input(":")
            break

        elif q == "n":
            city = None
            break

        else:
            print("Такоі команди не існує", "\n")

    db.create_user(name, surname, email, phone, city, password)
    print("Вітаємо ви створили аккаунт!", "\n")


def show_game_list():
    for row in db.all_games_and_price():
        title, price = row
        print("Назва гри:", title, "- Ціна:", price)


def loggin():
    while True:
        print("Введіть свій емейл")
        email = input(":")
        print("Введіть свій пароль")
        password = input(":")

        if db.check_email_and_password(email, password):
            print("Вітаємо, ви увійшли в свій аккаунт!", "\n")
            break
        else:
            print("Пароль або емпейл для цього аккаунту введений неправильно", "\n")


def add_to_cart():
    while True:
        print("Який товар ви хочете додати до кошика")
        item = input(":")
        item_id = db.items_id(item)
        if item_id:
            db.insert_id(item_id)
        else:
            print("Такого товару не існує")
    

    


def is_logged():
    while True:
        print("Яку дію ви хочете виконати?\n")
        print("1 - пошук відео гри по назві")
        print("2 - відобразити список ігор")
        print("3 - вихід з аккаунту")
        q = input(":")
        if q == "1":
            search_game()

        elif q == "2":
            show_game_list()

        elif q == "3":
            break
        else:
            print("Такої команди не існує")



add_to_cart()

while True:
    print("Яку дію ви хочете виконати?\n")
    print("1 - створення аккаунту")
    print("2 - вхід в аккаунту")
    print("3 - вихід з програми")

    q = input(":")

    if q == "1":
        create_account()
        is_logged()

    elif q == "2":
        loggin()
        is_logged()
    elif q == "3":
        break

    else:
        print("Такої команди не існує", "\n")
