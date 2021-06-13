from os import system, name

from time import sleep

def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

import math
diameter = 0
circumferance = 0
area = 0
case = 1
reask = 0

while True:
    case = int(input("Type '1' for area or type '2' for circumferance: "))
    if case == 1:
      diameter = int(input("What's the diameter of the circle? " ))
      print ("Diameter:", diameter)
      radius = int(diameter / 2)
      print("Radius is:", radius)
      area = math.pi * radius ** 2
      print("Area of the circle is:", area)
    elif case == 2:
      diameter = int(input("What's the diameter of the circle? "))
      print("Diameter", diameter)
      radius = int(diameter / 2)
      print("Radius is:", radius)
      circumferance = 2 * math.pi * radius
      print("Circumferance of the circle is:", circumferance)
    while True:
        reask = str(input("New Calculation? (y/n): "))
        if reask in ("y", "n"):
            break
        print("invalid input.")
    if reask == "y":
        sleep(1)
        clear()
        continue
    else:
        sleep(0.5)
        print("Goodbye. Thanks for calculating!")
        break
 