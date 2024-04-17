#підключення бібліотеки sqlite3 для роботи з базами даних
import sqlite3


#створення классу ShopDB для взаємодії з базою даних
class ShopDB:
    #параметри обьекту
    def __init__(self, dbname):
        #встановлення звязку з базою даних
        self.connection = sqlite3.connect(dbname)
        #створення обьекту звязку з базою даних
        self.cursor = self.connection.cursor()

    #я не буду писати пояснення для кожної функції тут тому що частіше вони виконують дуже вюзьконаправлену задачу
    def is_email_exist(self, email):
        self.cursor.execute('''SELECT email FROM clients WHERE email=?''', [email])
        is_email = self.cursor.fetchone()
        return is_email
    
    def is_phone_exist(self, phone):
        self.cursor.execute('''SELECT phone FROM clients WHERE phone=?''', [phone])
        is_phone = self.cursor.fetchone()
        return is_phone
    
    def create_user(self,name,surname,email,phone,city,password):
        self.cursor.execute('''INSERT INTO clients("name", "surname", "email", "phone", "city", "password")
                      VALUES(?,?,?,?,?,?)''',
                      [name,surname,email,phone,city,password])
       
        self.connection.commit()

    def check_email_and_password(self, email, password):
        self.cursor.execute('''SELECT password FROM clients WHERE email = ? AND password = ?''', (email, password))
        user = self.cursor.fetchone()
        return user

    def search_email(self, game_title):
        self.cursor.execute(
        '''SELECT quantity, title, price, description, category, developer, platform FROM items WHERE title = ?''', (game_title,))
        data = self.cursor.fetchall()
        return data
    def all_games_and_price(self):
        self.cursor.execute("""SELECT title, price FROM items""")
        data = self.cursor.fetchall()
        return data
    
    def items_id(self, item):
        self.cursor.execute('''SELECT id FROM items WHERE title = ?''', [item])
        item_db = self.cursor.fetchone()
        return item_db
    
    def add_item_to_cart(self, order_id, item_id, quantity):
        self.cursor.execute('''INSERT INTO cart(order_id, item_id, quantity)
                            VALUES(?,?,?)''',
                            [order_id, item_id, quantity])
        self.connection.commit()
    
    def create_order(self, client_id):
        self.cursor.execute('''INSERT INTO orders("client_id")
                            VALUES(?)''',
                            [client_id])
        self.connection.commit()
        return self.cursor.lastrowid
    
    def search_id_in_emails(self, email):
        self.cursor.execute("""SELECT id FROM clients WHERE email = ?""", (email,))
        data = self.cursor.fetchone()
        return data
    
    def game_price(self, cart_item):
        self.cursor.execute("""SELECT price FROM items WHERE title = ?""", (cart_item,))
        data = self.cursor.fetchone()
        return data