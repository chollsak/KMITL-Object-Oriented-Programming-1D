class ATM:
    def __init__(self, atm_id, cash_100, cash_500, cash_1000):
        self.__atm_id = atm_id
        self.__cash_100 = cash_100
        self.__cash_500 = cash_500
        self.__cash_1000 = cash_1000

    def insert_card_interac(self,user_name, account_id, pin):
        print("Your name is %s" %user_name)
        print("Your account id is %d" %account_id)
        is_insert = input("Please insert your card (Y/N): ")
        if is_insert == 'y':
            keying_pin = int(input("Enter your pin: "))
            if keying_pin == pin :
                print("Account Correct")
                user1.transaction_page_showing()
            else: 
                print("Account Incorrect")   
        else:
            print("Cancle by user")

    def device_cash_100(self):
        pass

    def device_cash_500(self):
        pass

    def device_cash_1000(self):
        pass   

    def transaction_page_showing(self):
        print("Select transaction")
        print("1. Withdraw Cash")
        print("2. Deposite Cash")
        print("3. Transfer Cash")
        temp_choice = int(input("transaction(1,2,3): "))
        if temp_choice == 1:
            atm.withdraw_action()
        elif temp_choice == 2:
            atm.deposite_action()
        elif temp_choice == 3:
            pass
        else:
            print("Error, Invalid number please try again")

    def withdraw_action(self):
        print("Available balance: %d" %saving_account.get_remain_cash())
        temp_withdraw_key = int(input("Enter amount to withdraw: "))
        if temp_withdraw_key > saving_account.get_remain_cash():
            print("Not enough money in your account!!!")
        else:
            total_atm_cash = (self.__cash_100*100) + (self.__cash_500*500) + (self.__cash_1000*1000)
            atm_balance = total_atm_cash - temp_withdraw_key
            temp_balance = saving_account.get_remain_cash() - temp_withdraw_key
            print("Complete!,Please get your cash.")
            print("Balance: %d" %temp_balance)
            print("ATM Balance: %d" %atm_balance)
            temp_withdraw_history = ("-%d" %temp_withdraw_key)
            saving_account._withdraw_history = temp_withdraw_history

    def deposite_action(self):
        print("Available balance: %d" %saving_account.get_remain_cash())
        temp_withdraw_key = int(input("Enter amount to deposite: "))
        total_atm_cash = (self.__cash_100*100) + (self.__cash_500*500) + (self.__cash_1000*1000)
        temp_balance = temp_withdraw_key + saving_account.get_remain_cash()

        atm_balance = total_atm_cash + temp_balance

        print("Complete! Thank you")
        print("Your balance: %d" %temp_balance)
        print("ATM Balance : %d" %atm_balance)



class User(ATM):
    def __init__(self, user_name, account_id, pin):     
        self.__user_name = user_name
        self.__account_id = account_id
        self.__pin = pin

    def insert_card(self):
        return super().insert_card_interac(self.__user_name, self.__account_id, self.__pin)    
             
class Card(User):
    def __init__(self, card_id, expire_date,user_name, account_id):
        super.__init__(user_name, account_id)
        self.__card_id = card_id
        self.__expire_date = expire_date
            
class Saving_Account(User):
    def __init__(self, remain_cash, withdraw_history, deposite_history, transfer_history, status):
        self.__remain_cash = remain_cash
        self._withdraw_history = withdraw_history
        self.__deposite_history = deposite_history
        self.__transfer_history = transfer_history
        self.__status = status

    def get_remain_cash(self):
        return self.__remain_cash

        
                
atm = ATM(65010195, 100, 100, 100)
user1 = User("Chollasak", 65010195, 1950)
saving_account = Saving_Account(1000, "none", "none", "none", "none")

print(saving_account._withdraw_history)

user1.insert_card()

