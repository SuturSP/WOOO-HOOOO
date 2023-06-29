class BankAccount:
    def __init__(self, owner_name, account_number, balance, password):
        self.owner_name = owner_name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Неправильный пароль"

    def set_balance(self, password, new_balance):
        if password == self.__password:
            self.__balance = new_balance
            return "Баланс успешно изменен"
        else:
            return "Неправильный пароль"


#Вы можете создать экземпляр класса BankAccount следующим образом и использовать его методы:

account = BankAccount("Иванов Иван", 123456789, 1000, "mypassword")

print(account.owner_name)
print(account.account_number)

print(account.get_balance("mypassword"))
print(account.set_balance("mypassword", 1500))
print(account.get_balance("mypassword"))

print(account.get_balance("wrongpassword"))
print(account.set_balance("wrongpassword", 2000))
