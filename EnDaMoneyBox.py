#Import all needed modules
from Modules.Style import *
from Modules.MoneyBox import *

#Define a banner 
banner = """
    ▒█▀▀▀ █▀▀▄ ▒█▀▀▄ █▀▀█   ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ █░░█ ▒█▀▀█ █▀▀█ █░█ 
    ▒█▀▀▀ █░░█ ▒█░▒█ █▄▄█   ▒█▒█▒█ █░░█ █░░█ █▀▀ █▄▄█ ▒█▀▀▄ █░░█ ▄▀▄ 
    ▒█▄▄▄ ▀░░▀ ▒█▄▄▀ ▀░░▀   ▒█░░▒█ ▀▀▀▀ ▀░░▀ ▀▀▀ ▄▄▄█ ▒█▄▄█ ▀▀▀▀ ▀░▀
"""

def keyboard_handler(passing=True):
    try:
        enter()
        exiting = input(Fore.RESET + f"    [{Fore.RED}?{Fore.RESET}]" + Fore.LIGHTRED_EX + " Do you want to do exit the program? (Y/N)" + Fore.RESET + " >> ")
        enter()
        if str(exiting).lower() in ("y","yes","yeah","stay","ja"):
            try:
                print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.WHITE + "]" + Fore.WHITE + " >> " + Fore.LIGHTBLUE_EX + "Roger that, exiting the EnDa MoneyBox!" + Fore.RESET)
                time.sleep(2)
                exit()
            except:
                exit()
        elif str(exiting).lower() in ("n","no","exit","quit","nein"):
            if passing:
                pass
            else:
                start_up()
        else:
            print(Fore.WHITE + "    [" + Fore.RED + "!" + Fore.WHITE + ']' + Fore.RED + " ERROR" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "The inputed option does not exist!" + Fore.RESET)
            keyboard_handler()
    except KeyboardInterrupt:
        keyboard_handler()
    except EOFError:
        keyboard_handler()

#Define a space var
space = "    "

#Define a function which checks if user want anther operation
def continues():
    enter()
    wanna_exit = input(Fore.WHITE + "    [" + Fore.YELLOW + "?" + Fore.WHITE + "]" + Fore.LIGHTYELLOW_EX + " Do you want to go back to main menu?" + Fore.WHITE + " >> ")
    if wanna_exit.lower() in ("n","no","nein","nah") or "n" in wanna_exit.lower():
        try:
            enter()
            programinput = 0
            print(Fore.WHITE + "    [" + Fore.BLUE + "!" + Fore.WHITE + "] >> " + Fore.LIGHTCYAN_EX + "Exiting the application..." + Fore.RESET)
            time.sleep(2)
            exit()
        except KeyboardInterrupt:
            exit()
    else:
        enter()
        options()

#Define a function which gets the first option
def operation():
    while True:
        print(space + Fore.WHITE + "[" + Fore.MAGENTA + "1" + Fore.WHITE + "] >> " + "Add a new transaction" + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.MAGENTA + "2" + Fore.WHITE + "] >> " + "See your transactions" + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.MAGENTA + "3" + Fore.WHITE + "] >> " + "See your balance" + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.YELLOW + "9" + Fore.WHITE + "] >> " + Fore.LIGHTYELLOW_EX + "Exit / Restart the Program" + Fore.RESET)
        enter()
        option = input(space + Fore.WHITE + "[" + Fore.BLUE + "*" + Fore.WHITE + "]" + Fore.CYAN + " Option" + Fore.WHITE + " >> " + Fore.RESET)
        try:
            int(option)
        except:
            enter()
            print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "Inputed option does not exist!" + Fore.RESET)
            enter()
        else:
            if int(option) in (1,2,3,9):
                return int(option)
            else:
                enter()
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "Inputed option does not exist!" + Fore.RESET)
                enter()    

#Define a function about the options
def options():
    if os.name in ("dos","nt"):
            os.system(f"title EnDa MoneyBox ^| Balance : {EnDaMoneyBox.get_balance()} $ ^| EnDaTeam on GITHUB")
    option = operation()
    enter()
    if option == 1:
        operative = 1
        while operative:
            add_minus = input(space + Fore.WHITE + "[" + Fore.YELLOW + "?" + Fore.WHITE + f"] The money were withdrawn ({Fore.RED}-{Fore.WHITE}) from or added ({Fore.GREEN}+{Fore.WHITE}) to your bank account? >> " + Fore.LIGHTMAGENTA_EX)
            if "+" in add_minus or "-" in add_minus:
                operative = 0
            else:
                enter()
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "Please input (+) for adding and (-) for withdrawing!" + Fore.RESET)
                enter()
        bal = EnDaMoneyBox.get_balance()
        bal = float(bal)
        amountinput = 1
        while amountinput:
            enter()
            amount = input(space + Fore.WHITE + "[" + Fore.YELLOW + "?" + Fore.WHITE + "] The amount of money? >> " + Fore.LIGHTGREEN_EX)
            try:
                print(Fore.RESET,end="")
                float(amount)
            except:
                enter()
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "Please input a float number as amount!" + Fore.RESET)
                enter()
            amount = float(amount)
            if amount > float(bal) and add_minus == "-":
                enter()
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + f"You don't have that much money! Your balance : {Fore.LIGHTGREEN_EX}{bal} $" + Fore.RESET)
                continue
            elif float(amount) == 0.0:
                enter()
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + f"You can't do transaction operation with 0 $" + Fore.RESET)
                continue
            else:
                if add_minus == "+":
                    bal = bal + float(amount)
                    amountinput = 0
                else:
                    bal = bal - float(amount)
                    amountinput = 0
            enter()
            note = input(space + Fore.WHITE + "[" + Fore.YELLOW + "?" + Fore.WHITE + "] Do you want to add a note? (Leave blank if you don't) >> " + Fore.RESET)
            if note.lower() in (" ", "") or "n" in note.lower():
                note = "NULL"
        if EnDaMoneyBox.add_newtransaction(amount,add_minus,bal,note):
            enter()
            print(space + Fore.WHITE + "[" + Fore.GREEN + "!" + Fore.WHITE + "] >> " + Fore.LIGHTGREEN_EX + "Your new transaction was recorded!" + Fore.RESET)
        else:
            try:
                enter()
                print(space,end="")
                error("SOMETHING WENT WRONG! It's suggested to have a talk with admin!")
                time.sleep(10)
                exit()
            except KeyboardInterrupt:
                exit()
        continues()
        options()
    elif option == 2:
        results = EnDaMoneyBox.get_transactions()
        for i in results:
            if i[0] == 0 and len(results) <= 1:
                print(space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "You don't have any recorded transaction yet!" + Fore.RESET)
            elif i[0] == 0:
                pass
            else:
                print(space + transaction_reader(i))
        continues()
        options()
    elif option == 3:
        date = EnDaMoneyBox.get_dateofaccount()
        date = date[0]
        balance = EnDaMoneyBox.get_balance()
        final = EnDaMoneyBox.get_finaltransaction()
        dates = str(date[0]) + "/" + str(date[1]) + "/" + str(date[2])
        print(space + Fore.WHITE + "[" + Fore.CYAN + "#" + Fore.WHITE + "] >> Account creation date : " + Fore.LIGHTCYAN_EX + str(dates) + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.GREEN + "$" + Fore.WHITE + "] >> Balance : " + Fore.LIGHTGREEN_EX + str(balance)  + " $ " + Fore.RESET)
        print(space + Fore.WHITE + "[" + Fore.LIGHTRED_EX + "^" + Fore.WHITE + "] >> The last transaction : ")
        if final[0] == 0:
            print(space +space + Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "] >> " + Fore.LIGHTRED_EX + "You don't have any recorded transaction yet!" + Fore.RESET)
        else:
            print(space + space + transaction_reader(final))
        continues()
        options()
    elif option == 9:
        while True:
            try:
                exit_restart_input = input(space + Fore.WHITE + "[" + Fore.LIGHTMAGENTA_EX + "*" + Fore.WHITE + "]" + Fore.WHITE + f" Do you want to {Fore.LIGHTRED_EX}exit{Fore.WHITE} or {Fore.LIGHTYELLOW_EX}restart{Fore.WHITE} the app? ({Fore.LIGHTRED_EX}E{Fore.WHITE}/{Fore.LIGHTYELLOW_EX}R{Fore.WHITE})" + Fore.WHITE + " >> " + Fore.RESET)
                enter()
                if exit_restart_input.lower() in ("e","exit","quit"):
                    try:
                        print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.WHITE + "]" + Fore.WHITE + " >> " + Fore.LIGHTRED_EX + "Roger that, exiting the EnDa MoneyBox!" + Fore.RESET)
                        time.sleep(2)
                        exit()
                    except:
                        exit()
                elif exit_restart_input.lower() in ("e","r","exit","quit","restart","res","sleep"):
                    try:
                        print("    " + Fore.WHITE + "[" + Fore.BLUE + "!" + Fore.WHITE + "]" + Fore.WHITE + " >> " + Fore.LIGHTYELLOW_EX + "Roger that, restarting the EnDa MoneyBox!" + Fore.RESET)
                        time.sleep(2)
                        start_up()
                        break
                    except:
                        start_up()
                        break
                else:
                    print(space + Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] >> " + Fore.LIGHTYELLOW_EX + "")
                    enter()
            except KeyboardInterrupt:
                enter()
                keyboard_handler()
            except EOFError:
                enter()
                keyboard_handler()


#Create a start-up
def start_up():
    try:
        clearConsole()
        enter()
        print(banner_color(banner))
        enter()
        print(space + Fore.LIGHTYELLOW_EX + "[==================" + Fore.WHITE + " Welcome to EnDa MoneyBox " + Fore.LIGHTYELLOW_EX + "==================]" + Fore.RESET)
        print(space + Fore.LIGHTCYAN_EX + "[================" + Fore.WHITE + " The best Virtual Money Vault " + Fore.LIGHTCYAN_EX + "================]" + Fore.RESET)
        enter()
        verifier()
        if os.name in ("dos","nt"):
            os.system(f"title EnDa MoneyBox ^| Balance : {EnDaMoneyBox.get_balance()} $ ^| EnDaTeam on GITHUB")
        enter()
        options()
    except KeyboardInterrupt:
        enter()
        keyboard_handler(passing=False)
    except EOFError:
        enter()
        keyboard_handler(passing=False)
            


#Program runs when is main
if __name__ == "__main__":
    start_up()
    