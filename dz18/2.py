class Cloth:
  def __init__(self,itog1,itog2):
    self.itog1 = itog1
    self.itog2 = itog2
    print ( f'Общий расход ткани для пальто и костюма:{self.itog1+self.itog2}')

class Coat(Cloth):  # пальто
  reserved1 = 0
  def __init__(self, V):
    self.V = V
  @property
  def calculate(self):
    self.reserved1 = int(self.V / 6.5 + 0.5)
    return f'Общий расход ткани  для пальто:{self.reserved1}'

class Suit(Cloth):  # костюм
  reserved2 = 0
  def __init__(self,H):
    self.H = H
  @property
  def calculate(self):
    self.reserved2 =int( 2 * self.H + 0.3)
    return f'Общий расход ткани  для костюма:{self.reserved2}'


c = Coat(66)
s = Suit(66)
print(c.calculate)
print(s.calculate)
itog1 = c.reserved1
itog2 = s.reserved2
C=Cloth(itog1,itog2)

