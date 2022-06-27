
from time import sleep

ticketPrices = [0, 20.57, 30.54, 60.71, 80.94, 100.43, 50.89]
ticketAges = ["0", "10", "20", "30", "40", "50", "60"]
SIZE = 7
x = SIZE - 1

print("Hello & welcome to my first array program")
sleep(1.5)
print("Please insert your age, and the price of your ticket will be displayed: ")
ageInput = input()
while int(ageInput) < int(ticketAges[x]):   
    x = x - 1

print("Your age is between " + ticketAges[x] + " and " + ticketAges[x + 1] + " years old")
sleep(1.5)
print("The price of your ticket is £" , (ticketPrices[x]))
sleep(1.5)
print("Thank you for using this program, goodbye")