# Goal: Take user input, add a $5.00 fee, and print the total.
price_input = input("What is the item price? ")
delivery_fee = 5

total = int(price_input) + delivery_fee 
#input is a string and deilvery fee is int, so I matched those
print("Your total is: " + str(total))
# can only concatenate str (not "int") to str

