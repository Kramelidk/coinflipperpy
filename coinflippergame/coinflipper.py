import random
import os
import time

def printLogo():
   print("\033[33m" + r"""      
     _____      _       ______ _ _                       
    / ____|    (_)     |  ____| (_)                      
   | |     ___  _ _ __ | |__  | |_ _ __  _ __   ___ _ __ 
   | |    / _ \| | '_ \|  __| | | | '_ \| '_ \ / _ \ '__|
   | |___| (_) | | | | | |    | | | |_) | |_) |  __/ |   
    \_____\___/|_|_| |_|_|    |_|_| .__/| .__/ \___|_|   
                                  | |   | |              
                                  |_|   |_|              
   """ + "\033[35mmade with <3 by kramel" + "\033[0m")

balance = 250

def formatNumber(number):
   return f"{number:,}"

def clear():
   os.system("cls")

def saveBalance(balance):
   path = os.path.join(os.path.dirname(__file__), "data.txt")

   with open(path, "w") as file:
      file.write(str(balance))

def loadBalance():
   path = os.path.join(os.path.dirname(__file__), "data.txt")

   try:
      with open(path, "r") as file:
         return int(file.read())
   except FileNotFoundError:
      return 100

balance = loadBalance()

saveBalance(balance)

def invalidOption():
   print("\033[1A", end="")
   print("\033[2K", end="")
   print("Choose: \033[31mInvalid choice!\033[0m")
   time.sleep(1)

def balanceMenu():
   global balance
   clear()
   print(f"Balance: ${formatNumber(balance)}\n")
   while True:
      print("1. Top-Up")
      print("2. Exit")
      choice = input("Choose: ")
      if choice == "1":
         amount = input("Enter amount to top-up: ")
         try:
            amount = int(amount)
            balance += amount
            print("\n\033[32mTop-Up successful!\033[0m")
            time.sleep(2)
            break
         except Exception:
            print("\n\033[31mInvalid amount! (example: 485786)\033[0m")
            time.sleep(2)
            break
      else:
         break
   clear()


def mainMenu():
   global balance

   while True:
      printLogo()
      print("\n== \033[33mCoinFlipper\033[0m ==")
      print(f"Balance: ${formatNumber(balance)}\n")
      print("1. Play")
      print("2. Balance")
      print("3. Exit")

      while True:
         choice = input("\nChoose: ")

         if choice in ["1", "2", "3"]:
               break

         print("\033[1A", end="")
         print("\033[2K", end="")
         print("Choose: \033[31mInvalid choice!\033[0m")

      if choice == "1":
         clear()
         print("chose 1")

      elif choice == "2":
         balanceMenu()

      elif choice == "3":
         clear()
         print("Goodbye!")
         break

mainMenu()
