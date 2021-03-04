from people import Mexican
from people import PuertoRican

if __name__ == '__main__':
  edgar = Mexican()
  edgar.set_fname("edgar")
  edgar.set_lname("Saavedra Valleo")

  charlse = PuertoRican()
  charlse.set_fname("Charlie")
  charlse.set_lname("Saavedra")

  people = [
    edgar,
    charlse
  ]

  for person in people:
    print(f"{person.fname} is from {person.country}")
    print("what you making for food?")
    print(person.make_food())

  a = [1,2,3]
  b = a
  b[0] = 3
  print(a)