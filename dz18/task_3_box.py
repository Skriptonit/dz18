# Задание 3
# Создайте класс Box (посылка), у которого будет приватные атрибуты:
# postcode (номер отправления),
# name (имя отправителя),
# from_city (город отправителя),
# target_city (город назначения).
# Реализуйте методы, которые будут давать возможность доступа к приватным атрибутам.
# Реализуйте метод, который будет давать возможность менять город назначения
# Назовите модуль task_3_box и сохраните его

class Box :
    def __init__(self,postcode,name ,from_city,target_city, ):
        self.__name=name
        self.__from_city=from_city
        self.__target_city=target_city
        self.__postcode=postcode

    @property
    def get_postcode(self):
     return self.__postcode
    @property
    def get_name(self):
        return self.__name
    @property
    def get_from_city(self):
        return self.__from_city
    @property
    def get_target_city (self):
        return self.__target_city
    @get_target_city .setter
    def get_target_city(self, new_city):
        self.__target_city = new_city
        return self.__target_city

name1=Box(777,"Алексей ","Казань","Москва")
name2=Box(666,'Евгений','Воронеж','Исмаил')
name3=Box(555,'Михаил','Балтаси','Елабуга')
print ('1)',"Код заказа: ",name1.get_postcode,"Имя отправителя:",name1.get_name,"Откуда заказ:",name1.get_from_city," Куда доставить заказ:",name1.get_target_city)
print ('2)',"Код заказа: ",name2.get_postcode,"Имя отправителя:",name2.get_name," Откуда заказ:",name2.get_from_city,"Куда доставить заказ:",name2.get_target_city)
print ('3)',"Код заказа: ",name3.get_postcode,"Имя отправителя:",name3.get_name,"  Откуда заказ:",name3.get_from_city,"Куда доставить заказ:",name3.get_target_city)
name1.get_target_city='Нью-Йорк'
print("Новый адрес доставки посылки под кодом 777:",name1.get_target_city)
