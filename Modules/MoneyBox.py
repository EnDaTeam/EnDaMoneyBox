#Import needed module
from Modules.Style import *
import sqlite3
from datetime import datetime

#Space 
space = "    " 

#Define the main class
class EnDaMoneyBox():
    def __init__(self):
        pass

    #Define a function which creates the database file
    def create_databasefile():
        if not os.path.isfile("Database.db"):
            file = open("Database.db","w")
            return True
        return False
    
    #Define a function which creates the Transactions Table
    def create_transactiontable():
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE transactions(id, amount, operation, day, month, year, hour_min, banknote, balance);")
            cur.execute(f"""INSERT INTO transactions VALUES(0, 0 ,"+", {datetime.today().strftime("%d")} ,{datetime.today().strftime("%m")}, {datetime.today().strftime("%Y")}  ,"{datetime.now().strftime("%H:%M")}", 0, 0);""")
            con.commit()
            return True
        except:
            return False
        
    #Define a function which gets the transactions info from table
    def get_transactions():
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM transactions")
            rows = cur.fetchall()
            return rows
        except:
            return False
        
    #Define a function which gets the final balance of the account
    def get_balance():
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT balance FROM transactions ORDER BY id DESC LIMIT 1")
            balance = cur.fetchall()
            return balance[0][0]
        except:
            return False
        
    #Define a function which gets the date of the final transaction
    def get_finaltransaction():
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM transactions ORDER BY id DESC LIMIT 1")
            row = cur.fetchall()
            return row[0]
        except:
            return False
        
    #Define a function which gets the date of creation the account
    def get_dateofaccount():
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute("SELECT day, month, year FROM transactions WHERE id = 0")
            row = cur.fetchall()
            return row
        except:
            return False
    
    #Define a function which adds a new transaction
    def add_newtransaction(amount: float, operation: str, balance_after: int, banknote: float = 1):
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            id = int(EnDaMoneyBox.get_finaltransaction()[0]) + 1
            query = """INSERT INTO transactions VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            values = (id, amount, operation, datetime.today().strftime("%d"), datetime.today().strftime("%m"),
                    datetime.today().strftime("%Y"), datetime.now().strftime("%H:%M"), banknote, balance_after)
            cur.execute(query, values)
            con.commit()
            return True
        except:
            return False

    #Define a function which gets the number of a type of banknote only for positive 
    def get_theAmountBanknotePositive(type:float=1):
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute(f"""SELECT SUM(amount) FROM transactions WHERE banknote = {type} and operation = "+" """)
            row = cur.fetchall()
            return row[0][0]
        except:
            return False
        
    #Define a function which gets the number of a type of banknote only for negative 
    def get_theAmountBanknoteNegative(type:float=1):
        try:
            con = sqlite3.connect("Database.db")
            cur = con.cursor()
            cur.execute(f"""SELECT SUM(amount) FROM transactions WHERE banknote = {type} and operation = "-" """)
            row = cur.fetchall()
            if row[0][0] == None:
                return 0
            return row[0][0]
        except:
            return False    

#Define a function which reads the transactions and transform it to a text
def transaction_reader(lista:list):
    transaction = Fore.WHITE + "["
    action = "withdrawn from"
    if lista[2] == "+":
        transaction = transaction + Fore.GREEN + "+"
        action = "added to"
    else:
        transaction = transaction + Fore.RED + "-"
    transaction = transaction + Fore.WHITE + "] >> " + f"ID : {Fore.CYAN}{lista[0]}{Fore.WHITE} | {Fore.LIGHTYELLOW_EX}{lista[1]}{Fore.WHITE} $ were {action} your account on {Fore.LIGHTMAGENTA_EX}{lista[3]}/{lista[4]}/{lista[5]}{Fore.WHITE} at {Fore.LIGHTMAGENTA_EX}{lista[6]}{Fore.WHITE}"
    if not lista[7] == "NULL":
        transaction = transaction + f" | Banknote : {Fore.LIGHTWHITE_EX} {lista[7]}{Fore.WHITE}"
    transaction = transaction + f" | Balance after : {Fore.LIGHTGREEN_EX}{lista[8]}{Fore.WHITE}"
    return transaction

#Define a function which verifies if the workspace was done
def verifier():
    if EnDaMoneyBox.create_databasefile():
        print(space + Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "] >> " + Fore.LIGHTGREEN_EX + "Database created!" + Fore.RESET)
    if EnDaMoneyBox.create_transactiontable():
        print(space + Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "] >> " + Fore.LIGHTGREEN_EX + "Tables organized!" + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] >> " + Fore.LIGHTYELLOW_EX + "You don't have any transaction!" + Fore.RESET)