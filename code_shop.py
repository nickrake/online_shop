import sqlite3
connection = sqlite3.connect("shop.db")
cursor = connection.cursor()



while True:
    print("Яку дію ви хочете виконати?\n")
    print("1 - пошук відео гри по назві")
    print("2 - вихід з програми")

    q = input(":").strip().lower()

    if q == "1":
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
            print("Відео гра з такою назвою не знайдена")

    elif q == "2":
             break
    

    else:
        print("Такоі команди не існує")