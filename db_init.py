import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('CreditX.db')
c = conn.cursor()

# # List of tables to be dropped
# tables = ["USER", "CARDS", "PAYMENTS", "FEEDBACK"]
#
# # Drop each table if it exists
# for table in tables:
#     c.execute(f"DROP TABLE IF EXISTS {table};")
#     print(f"Table {table} dropped.")

# Create USER table
conn.execute('''
CREATE TABLE IF NOT EXISTS USER (
    UserID INTEGER PRIMARY KEY,
    Name TEXT,
    Password TEXT
);
''')
print('USER table created...')

# Create CARDS table
conn.execute('''
CREATE TABLE IF NOT EXISTS CARDS (
    CardID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Name TEXT,
    CardNo TEXT,
    Bank TEXT,
    Balance INTEGER,
    FOREIGN KEY (UserID) REFERENCES USER(UserID)
);
''')
print('CARDS table created...')

# Create PAYMENTS table
conn.execute('''
CREATE TABLE IF NOT EXISTS PAYMENTS (
    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Name TEXT,
    PaymentAmt INTEGER,
    Recipient TEXT,
    CardNo TEXT,
    Date TEXT,
    FOREIGN KEY (UserID) REFERENCES USER(UserID)
);
''')
print('PAYMENTS table created...')

# Create FEEDBACK table
conn.execute('''
CREATE TABLE IF NOT EXISTS FEEDBACK (
    FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    Name TEXT,
    ui_good TEXT,
    ui_rating INTEGER,
    f_good TEXT,
    f_rating INTEGER,
    best_f TEXT,
    ov_rat INTEGER,
    comm TEXT,
    FOREIGN KEY (UserID) REFERENCES USER(UserID)
);
''')
print('FEEDBACK table created...')

# Commit the changes and close the connection
conn.commit()
conn.close()
