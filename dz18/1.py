# Задание 1
# Сооздайте класс Person с приватными атрибутами name, age, surname.
# Реализуйте методы name, age, surname, которые будут давать доступ к аналогичным приватным атрибутам.
# Создайте сеттер, который будет давать возможность поменять атрибут age.

class Person ():
    def __init__(self, name,age,surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def get_name(self, new_name):
        self.__name = new_name
        return self.__name

    @property
    def get_surname (self):
        return self.__surname
    @get_surname .setter
    def get_surname (self, new_surname):
        self.__surname = new_surname
        return self.__surname

    @property
    def get_age(self):
        return self.__age
    @get_age.setter
    def get_age(self, new_age):
        self.__age = new_age
        return self.__age

p= Person("Роналду",37,"Криштиану")
print (p.get_surname,p.get_name,p.get_age)
p.get_surname = "Лионель"
p.get_name='Месси'
p.get_age=35
print (p.get_surname,p.get_name,p.get_age)