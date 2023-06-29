class ExampleClass:
    def public_method(self):
        print("Это открытый (public) метод")
        self.__private_method()

    def __private_method(self):
        print("Это закрытый (private) метод")


example = ExampleClass()
example.public_method()
