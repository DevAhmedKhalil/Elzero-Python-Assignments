import sqlite3


def create_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        conn.close()
        print(f"Database {db_name} created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")


def create_table(db_name, table_name, fields):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(fields)})")
        conn.commit()
        conn.close()
        print(f"Table {table_name} created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_users(db_name, table_name, names, emails, dates):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        for key, user in enumerate(names):
            birthdate = dates[key]
            email = emails[key]
            cursor.execute(f"INSERT INTO {table_name} (name, birthdate, email) VALUES (?, ?, ?)",
                           (user, birthdate, email))
            print(f"Data added successfully for {user}")
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as e:
        print(f"Error adding data: {e}")


def delete_user(db_name, table_name, user_id):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id=?", (user_id,))
        conn.commit()
        conn.close()
        print("User Deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")


def show_users(db_name, table_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} ORDER BY id")
        remaining_users = cursor.fetchall()
        print("Show Other Data:")
        for user in remaining_users:
            print(f"ID => {user[0]}, Name => {user[1]}, Date Of Birth => {user[2]}, Email => {user[3]}")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error showing users: {e}")


# Usage example:
db_name = 'elzero.db'
table_name = 'users'
fields = ['id INTEGER PRIMARY KEY', 'name TEXT UNIQUE', 'birthdate DATE', 'email TEXT UNIQUE']

create_database(db_name)
create_table(db_name, table_name, fields)

my_list_names = ["Ahmed", "Sayed", "Gamal", "Mahmoud", "Kamel"]
my_list_emails = ["a@gmail.com", "s@gmail.com", "g@gmail.com", "m@gmail.com", "k@gmail.com"]
my_list_date = ['20/10/1989', '12/02/1989', '13/03/1989', '14/04/1989', '15/05/1989']

insert_users(db_name, table_name, my_list_names, my_list_emails, my_list_date)
delete_user(db_name, table_name, '1')  # Example, delete user with ID '1'
show_users(db_name, table_name)
