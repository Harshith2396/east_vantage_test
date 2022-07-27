import sqlite3


class Database:   # this class we be used as a module
    def __init__(self):
        if __name__ == "__main__":
            self.connection = sqlite3.connect("./database.db")
        else:
            self.connection = sqlite3.connect("./db/database.db", check_same_thread=False)

        self.cursor = self.connection.cursor()

    def insertOne(self, name: str, city: str, coordinates: str):  # method to insert data
        queryData = [name, city, coordinates]
        self.cursor.execute("INSERT INTO address(name, city, coordinates) VALUES(?, ?, ?)", queryData)
        self.connection.commit()

    def getData(self):  # method to get data
        self.cursor.execute("SELECT * FROM address")
        return self.cursor.fetchall()

    def updateData(self, id: int, data: list):  # method to update data
        self.cursor.execute(
            f"UPDATE address SET name='{data[0]}', city='{data[1]}', coordinates='{data[2]}' WHERE id={id}")
        self.connection.commit()

    def deleteOFromDb(self, id: int):  # method to delete data
        self.cursor.execute(f"DELETE FROM address WHERE id = {id}")
        self.connection.commit()


if __name__ == "__main__":
    Database()

"""self.cursor.execute("CREATE TABLE Address(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, city TEXT NOT NULL, coordinates TEXT NOT NULL)")"""
