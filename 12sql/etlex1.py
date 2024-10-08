import mysql.connector
from password import parola
import pandas as pd

# analiza comenzi din magazin online
# 1. extragere

my_db = mysql.connector.connect(
    database='grupa22',
    host='localhost',
    user='root',
    password=parola
)

cursor = my_db.cursor()

# cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name VARCHAR(100),'
#                'category VARCHAR(50),'
#                'price DECIMAL(10, 2))')
#
# cursor.execute('CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'product_id INT,'
#                'quantity INT,'
#                'order_date DATE,'
#                'FOREIGN KEY(product_id) REFERENCES products(id))')

# sql = "INSERT INTO products (name, category, price) VALUES (%s, %s, %s)"
# val = [
#     ('Laptop', 'Electronice', 1500.00),
#     ('Telefon', 'Electronica', 800.00)
# ]
# cursor.executemany(sql, val)
# my_db.commit()
#
# sql = "INSERT INTO orders (product_id, quantity, order_date) VALUES (%s, %s, %s)"
# val = [
#     (1, 2, '2023-09-01'),
#     (2, 1, '2023-09-02')
# ]
# cursor.executemany(sql, val)
# my_db.commit()

# 2 transform
query = ("SELECT "
         "o.id, p.name, p.category, o.quantity, p.price "
         "FROM orders o JOIN products p ON o.product_id = p.id")
df = pd.read_sql(query, my_db)
print(df)

df['total'] = df['quantity'] * df['price']
print(df)
# load
df.to_csv('raport_vanzari.csv', index=False)

# cursor.execute('CREATE TABLE raport_vanzari (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'name varchar(100),'
#                'category VARCHAR(50),'
#                'quantity INT,'
#                'price DECIMAL(10, 2),'
#                'total DECIMAL(10, 2))')

sql = "INSERT INTO raport_vanzari (name, category, quantity, price, total) VALUES (%s, %s, %s, %s, %s)"
lista = []
for item, row in df.iterrows():
    lista.append(row.tolist()[1:])
cursor.executemany(sql, lista)
my_db.commit()
