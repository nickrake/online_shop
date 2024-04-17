#підключення классу ShopDB з файлу sql_scripts для взаємодії з базою даних
from sql_scripts import ShopDB

#створення обьекту классу ShopDB
db = ShopDB("shop.db")

#стан заказу
current_order = None
#стан користувача
current_user = None

#створення классу "замовлення"
class Order:

    #параметри обьекту
    def __init__(self, client_id):
        self.client_id = client_id
        self.cart_items = []
        self.id = db.create_order(client_id)

    #функція додавання в кошик предмету
    def add_to_cart(self, cart_item, quantity):
        item_db = db.items_id(cart_item)
        if item_db:
            db.add_item_to_cart(self.id, item_db[0], quantity)
            price = float(db.game_price(cart_item)[0])
            total_price = price * float(quantity)
            self.cart_items.append({"Назва":cart_item, "Кількість":quantity, "Вартість":total_price})
            print("Товар додано в кошик")
            print(self.cart_items)
        else:
            print("Помилка")

    #функція показу вмісту кошика
    def show_cart(self):
        for item in self.cart_items:
            print(f"Товар: {item['Назва']}, Кількість:{item['Кількість']} - {item['Вартість']} грн")



#функція програми по пошуку гри по назві
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



#функція програми по створення аккаунту
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
    id = db.search_id_in_emails(email)
    return id



#функція програми по друкуванню списка всіх ігор та ціни
def show_game_list():
    for row in db.all_games_and_price():
        title, price = row
        print("Назва гри:", title, "- Ціна:", price)



#функція програми по реестрація в існуючій акаунт
def loggin():
    while True:
        print("Введіть свій емейл")
        email = input(":")
        print("Введіть свій пароль")
        password = input(":")

        user = db.check_email_and_password(email, password)
        if user:
            print("Вітаємо, ви увійшли в свій аккаунт!", "\n")
            id = db.search_id_in_emails(email)
            return id
     
        else:
            print("Пароль або емпейл для цього аккаунту введений неправильно", "\n")



#??? Навіщо потрібна фунція add_to_cart() якщо такаж функція є в класі Order ???

# def add_to_cart():
#     while True:
#         print("Який товар ви хочете додати до кошика")
#         item = input(":")
#         print("Кількість")
#         quantity = input(":")
#         db.add_item_to_cart(item, quantity)

#??? Навіщо потрібна фунція add_to_cart() якщо такаж функція є в класі Order ???



#інтерфейс взаємодаї з користувачем
while True:
    if not current_user:
        print("Яку дію ви хочете виконати?\n")
        print("1 - створення аккаунту")
        print("2 - вхід в аккаунту")
        print("3 - вихід з програми")

        q = input(":")

        if q == "1":
            id = create_account()
            current_user = "logged"

        elif q == "2":
            id = loggin()
            current_user = "logged"

        elif q == "3":
            break

        else:
            print("Такої команди не існує", "\n")
    elif current_user:
        print("Яку дію ви хочете виконати?\n")
        print("1 - пошук відео гри по назві")
        print("2 - відобразити список ігор")
        print("3 - додати в кошик")
        print("4 - вихід з аккаунту")
        q = input(":")
        if q == "1":
            search_game()

        elif q == "2":
            show_game_list()
        
        elif q == "3":
            if  not current_order:
                current_order = Order(id[0])
                while True:
                    print("Що зробити?")
                    print("1 - додати товар")
                    print("2 - підтвердити покупки")
                    q = input(":")
                    if q == "1":
                        print("Який товар ви хочете добавити")
                        cart_item = input(":")
                        print("Скільки цього товару добавити в кошик")
                        quantity = input(":")
                        current_order.add_to_cart(cart_item, quantity)
                    elif q == "2":
                        current_order = None
                        break
                    else:
                        print("Такої команди не існує")
            else:
                print("Помилка")
        elif q == "4":
            current_user = None
        else:
            print("Такої команди не існує")
    else:
        print("Не знаю як можно викликати цей елс але окей. ЦЕ ПОМИЛКА")