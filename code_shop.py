import sqlite3

def search_game():
     print("Введіть назву відео гри")
     game_title = input(":").lower()
     cursor.execute('''SELECT quantity, title, price, description, category, developer, platform FROM items WHERE title = ?''', (game_title,))
     data = cursor.fetchall()
     if data:
           for row in data:
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
              cursor.execute('''SELECT email FROM clients WHERE email=?''', [email])
              is_email = cursor.fetchone()

              if is_email:
                     print("Аккаунт з таким емейлом вже існує", "\n")
              else:
                     break

       while True:
              print("Введіть свій номер телефону")
              phone = input(":")
              cursor.execute('''SELECT phone FROM clients''')
              data = [row[0] for row in cursor.fetchall()]                #?????????????????????

              if phone in data:
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
                     


       cursor.execute('''INSERT INTO clients("name", "surname", "email", "phone", "city", "password")
                      VALUES(?,?,?,?,?,?)''',
                      [name,surname,email,phone,city,password])
       
       connection.commit()

       print("Вітаємо ви створили аккаунт!", "\n")
                      

def show_game_list():
      cursor.execute("""SELECT title, price FROM items""")
      data = cursor.fetchall()
      for row in data:
            title, price = row
            print("Назва гри:", title, "- Ціна:", price)
      

def loggin():
    while True:
        print("Введіть свій емейл")
        email = input(":")
        cursor.execute('''SELECT password FROM clients WHERE email = ?''', (email,))
        data = cursor.fetchone()  

        if data:
            print("Введіть свій пароль")
            password = input(":")
            if password == data[0]: 
                print("Вітаємо, ви увійшли в свій аккаунт!", "\n")
                break
            else:
                print("Пароль для цього аккаунту введений неправильно", "\n")
        else:
            print("Аккаунт з таким емейлом не існує")


def add_to_cart():
      print("Який товар ви хочете додати до кошика")  
      item =input(":")
      cursor.execute('''SELECT id FROM items WHERE title = ?''', [item])
      item_db = cursor.fetchone()
      if item_db:
            





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
        


         



connection = sqlite3.connect("shop.db")
cursor = connection.cursor()



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