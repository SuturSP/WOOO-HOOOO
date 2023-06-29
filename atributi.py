class Person:
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Возраст не может быть отрицательным")

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


person = Person(25, "John")
print(person.get_age())
print(person.get_name())

person.set_age(30)
person.set_name("Mike")

print(person.get_age())
print(person.get_name())

person.set_age(-10)


#В этом примере, при вызове метода set_age(), передается новое значение возраста.
# Если значение больше или равно нулю, оно присваивается атрибуту _age.
# Если переданное значение меньше нуля, выводится сообщение об ошибке.

#Методы get_age() и get_name() просто возвращают значения атрибутов _age и _name соответственно.
