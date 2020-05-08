# Outfit Picker
# Kenjie De Castro
# Version 1.0 - 5/4/20
# This program will allow you to input outfit choices and then once inputation

print ("Hello! Welcome to the 'Fit' Randomizer Generator.")

import random
Cont = "Y"

Fits = []


while Cont == "Y":
  while True:
    OutfitChoice = input("\nPlease enter a fit (Input 0 to end): ")
    if OutfitChoice == "0":
      break
    else:
      Fits.append(OutfitChoice)

  print("\nYour fit for today is: " + Fits[random.randint(0,len(Fits)-1)])

  Cont = input("Would you like to randomize another choice? (Y or N): ")

  # IDEA: Your outfit for today is, all inputs that were randomized