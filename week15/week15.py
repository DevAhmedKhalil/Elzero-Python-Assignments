# print("Assignment 01")

# VARCHAR/CHAR:
# ُستخدم لتخزين النصوص القصيرة، مع طول ثابت (CHAR) أو متغير (VARCHAR).

# INTEGER:
# تُستخدم لتخزين الأعداد الصحيحة، مثل أرقام الهوية أو العمر.

# FLOAT/DOUBLE:
# تستخدم لتخزين الأعداد العائمة (الأرقام العشرية)، مثل الأسعار أو الوزن.

# DATE/TIME:
# تستخدم لتخزين التواريخ أو الأوقات، مثل تواريخ الميلاد أو وقت الإنشاء.

# BOOLEAN:
# تستخدم لتخزين القيم المنطقية مثل صحيح أو خاطئ، نعم أو لا.


print("-" * 20)
print("Assignment 02")
print("-" * 20)

# Import SQLite Module
import sqlite3

# Database name
db_name = 'elzero.db'

# Create Database And Connect
db = sqlite3.connect(db_name)

# Setting Up The Cursor
cr = db.cursor()

# Table name and field names
table_name = 'users'
fields = ['id INTEGER PRIMARY KEY', 'name TEXT UNIQUE', 'birthdate DATE', 'email TEXT UNIQUE']

# Create the table if it doesn't exist
# cr.execute("create table if not exists users (id integer, name text, birthdate DATE, email TEXT)")
cr.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(fields)})")
print(f"Database {db_name} and Table {table_name} created successfully.")

# Inserting Users
my_list_names = ["Ahmed", "Sayed", "Gamal", "Mahmoud", "Kamel"]
my_list_emails = ["a@gmail.com", "s@gmail.com", "g@gmail.com", "m@gmail.com", "k@gmail.com"]
my_list_date = ['20/10/1989', '12/02/1989', '13/03/1989', '14/04/1989', '15/05/1989']

# try:
#     cr.execute(f"INSERT INTO {table_name} (name, birthdate, email) VALUES (?, ?, ?)",
#                    ('Ahmed', "20/10/1989", "a@gmail.com"))
# except sqlite3.IntegrityError as er:
#     print(f"Error DB... {er}")

print("-" * 50)
print("Assignment 03")
print("-" * 50)

# Adding name, email, date into DATABASE
# for key, user in enumerate(my_list_names):
#     birthdate = my_list_date[key]
#     email = my_list_emails[key]
#
#     try:
#         cr.execute(f"INSERT INTO {table_name} (name, birthdate, email) VALUES (?, ?, ?)", (user, birthdate, email))
#         print(f"Data added successfully for {user}")
#     except sqlite3.IntegrityError as e:
#         print(f"Error adding data: {e}")

# print("-" * 50)
# print("Assignment 04")
# print("-" * 50)

# # Last Row In table
# cr.execute(f"SELECT * FROM users ORDER BY id DESC LIMIT 1")
# last_row = cr.fetchone()
#
# print("Last ROW is: ")
# print(last_row)

print("-" * 50)
print("Assignment 05")

# Enter User ID TO Delete
user_id = input("Please enter the member ID to delete: ")

# Check If User Found
cr.execute(f"SELECT * FROM users WHERE id=?", (user_id,))
existing_user = cr.fetchone()

if existing_user:
    # Deleting existing user if it's Found
    cr.execute(f"DELETE FROM users WHERE id=?", user_id)
    print("User Deleted.")

    # Show All Info with order
    cr.execute(f"SELECT * FROM users ORDER BY id")
    remaining_users = cr.fetchall()

    # Show Other Data
    print("Show Other Data:")
    for user in remaining_users:
        print(f"ID => {user[0]}, Name => {user[1]}, Date Of Birth => {user[2]}, Email => {user[3]}")
else:
    print("User Not Found.")

# Commit the changes
db.commit()

# Close the connection
db.close()
