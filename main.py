#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator!")

total_bill = float(input("What is your total bill? $"))

tip_percent = int(input("How much would you like to tip? "))

num_people = int(input("How many people to split the bill? "))

price_per_person = (total_bill / num_people) * ((tip_percent / 100) + 1)

price_per_person = "{:.2f}".format(price_per_person)

print(f"Each person should pay: ${price_per_person}")


