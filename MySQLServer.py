import mysql.connector
def create_database():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Lulu0962081603'
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        print("Error creating database:", err)

if __name__ == "__main__":
    create_database()
