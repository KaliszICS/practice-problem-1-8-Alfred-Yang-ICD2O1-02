
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print (bool1 and bool2)
  print (bool1 or bool2) 
def q2():
  #Write Assignment code here
  num1 = int(input("Enter an integer: "))
  print (not num1 == 0)
def q3():
  #Write Assignment code here
  num2 = float(input("Enter a number: "))
  print (num2 >= 0 and num2 <= 10)
def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")
  food = food == "pizza"
  drink = drink == "pop"
  print (f"{ not(food and drink)}")
def q5():
  #Write Assignment code here
  num3 = int(input("Enter an integer: "))
  num4 = num3 % 2 == 0
  print (f"The integer {num3} is {num4}.")
#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
