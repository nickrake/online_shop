import sqlite3

class ShopDB:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

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
    
    def insert_id(self, item_id):
        self.cursor.execute('''INSERT INTO cart("item_id")
                            VALUES(?)''',
                            [item_id])
        self.connection.commit()