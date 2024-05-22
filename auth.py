import sqlite3


def create_user(userID, name, password):
    conn = sqlite3.connect('CreditX.db')
    try:
        conn.execute("Insert into USER(UserID, Name, Password) values(?, ?, ?);", (userID, name, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True


def authenticate_user(userID, name, password):
    conn = sqlite3.connect('CreditX.db')
    c = conn.cursor()
    c.execute("Select * from USER where Name = ? and Password = ?;", (name, password))
    user = c.fetchone()
    conn.close()
    return user is not None
