class Preson:
  def __init__(self, country=""):
    self.fname = ""
    self.lname = ""
    self.country = country

  def set_fname(self, name=""):
    self.fname = name

  def set_lname(self, name=""):
    self.lname = name
  
  def set_country(self, country=""):
    self.country = country

  def make_food(self):
    return ""

class Mexican(Preson):
  def __init__(self):
    super().__init__("Mexico")
  
  def make_tortillas(self):
    return f"hola soy {self.fname}, estoy haciendo tortillas"

  def make_food(self):
    return self.make_tortillas()

class PuertoRican(Preson):
  def __init__(self):
    super().__init__("Puerto Rico")

  def make_plantano(self):
    return f"hola soy {self.fname}, estoy haciendo platano"

  def make_food(self):
    return self.make_plantano()
