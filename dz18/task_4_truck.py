# Задание 4
# Реализуйте класс Truck (грузовик). Грузовик может перевозить посылки - Box из предыдущего задания
# Импортиуйте модуль task_3_box из предыдущего задания.
# Создайте несколько экземпляров класса Box.
# Проверьте работу методов класса Box
# Создайте класс Truck (грузовик), который будет иметь несколько атрибутов, присущих грузовику.
# Реализуйте атрибут capacity (емкость), в котором будет реализовано хранилище посылок (Box): [box1, box2 ...]
# Переопределите методы __str__, __add__, __sub__ для реализации отображения грузовика, загрузки и выгрузки посылок.
# Продемонстрируйте работу класса Truck.
from task_3_box import Box
name1= Box('111',"Роналду.","Дубай.","Мадрид.")
name2= Box('222',"Месси.","Париж.","Барселона.")
name3=Box('333',"Головин.","Монако.","Мадрид.")

Box=Box('111',"Роналду.","Дубай.","Мадрид.")
print ('1)',"Код заказа: ",name1.get_postcode,"Имя отправителя:",name1.get_name,"Откуда заказ:",name1.get_from_city," Куда доставить заказ:",name1.get_target_city)
print ('2)',"Код заказа: ",name2.get_postcode,"Имя отправителя:",name2.get_name,"  Откуда заказ:",name2.get_from_city," Куда доставить заказ:",name2.get_target_city)
print ('3)',"Код заказа: ",name3.get_postcode,"Имя отправителя:",name3.get_name,"Откуда заказ:",name3.get_from_city,"Куда доставить заказ:",name3.get_target_city)


class Car:
  def __init__(self, color, marka, kyzov, transmission):
    self.color = color
    self.marka = marka
    self.kyzov = kyzov
    self.transmission = transmission

  capacity=[]

  def __add__(self, get_postcode):
    self.capacity.append(get_postcode)

  def __sub__(self):
    self.capacity.pop(0)
  def __str__(self):
    return ','.join(self.capacity)
truck=Car("Синий","BMW","грузовик","Механика ")
print("Инфорация об авто :")
print("Марка -",truck.marka)
print("Цвет -",truck.color)
print("Кузов -",truck.kyzov)
truck +name1.get_postcode
print ('Добавим в грузовик посылку под кодом 111:',truck.capacity)
truck+name2.get_postcode
print ('Добвим в грузовик еще одну посылку , имеющий код 222:',truck.capacity)
truck+name3.get_postcode
print ('Чтобы грузовик поехал , надо добавить еще одну посылку :',truck.capacity)
truck.__sub__()
print ("О нет !Случился перегруз !Надо убрать одну посылку:",truck.capacity)
print ("Ура ! Можно отправляться в путь !")
print('После проделонной работы мы имеем в грузовике вот такие посылки:')
print (truck)