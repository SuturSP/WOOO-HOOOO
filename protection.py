class MyClass:
    def __init__(self):
        self.public_attribute = "Public"  # Публичный атрибут
        self._protected_attribute = "Protected"  # Защищенный атрибут
        self.__private_attribute = "Private"  # Приватный атрибут

    def public_method(self):
        return "This is a public method."

    def _protected_method(self):
        return "This is a protected method."

    def __private_method(self):
        return "This is a private method."


obj = MyClass()

# Доступ к публичным атрибутам и методам доступен извне класса
print(obj.public_attribute)
print(obj.public_method())
# Output:
# Public
# This is a public method.

# Доступ к защищенным атрибутам и методам возможен изнутри класса и его наследников
print(obj._protected_attribute)
print(obj._protected_method())
# Output:
# Protected
# This is a protected method.

# Попытка доступа к приватным атрибутам и методам извне класса вызовет ошибку
print(obj.__private_attribute)  # AttributeError: 'MyClass' object has no attribute '__private_attribute'
print(obj.__private_method())  # AttributeError: 'MyClass' object has no attribute '__private_method'


#В этом примере класс MyClass имеет три атрибута – public_attribute, _protected_attribute и __private_attribute,
# а также три метода – public_method(), _protected_method() и __private_method().

#- public_attribute – публичный атрибут, к которому можно получить доступ как извне класса, так и изнутри него.
#- _protected_attribute – защищенный атрибут, к которому можно получить доступ только изнутри класса или его наследников.
#- __private_attribute – приватный атрибут, к которому нельзя получить доступ извне класса или его наследников.

#Аналогично, для методов применяются аналогичные правила доступа.

#Использование различных степеней защиты позволяет контролировать доступность атрибутов и методов класса
# и обеспечить соблюдение инкапсуляции и модульности кода.
