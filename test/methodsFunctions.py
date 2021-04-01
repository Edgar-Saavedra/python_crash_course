class Car:

  def __init__(self, carcolor, type_car):
    self.carcolor = carcolor
    self.type = type_car
  
  def get_car_info(self):
    return {
      'carcolor': self.carcolor,
      'cartype': self.type,
    }
  
  def car_status(self):
    my_string = 'hi im doing good'
    return my_string

class Lambo(Car):
  def __init__(self, carcolor):
    super().__init__(carcolor, 'Lambo')

class Toyota(Car):
  def __init__(self, carcolor):
    super().__init__(f'#{carcolor}', 'Toyota')

lambo = Lambo('red')
toyota = Toyota('green')

print(lambo.get_car_info())
print(toyota.get_car_info())