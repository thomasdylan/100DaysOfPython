#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is the total of the bill? "))
percent = 1 + (float(input("What percentage would you like to tip? ")) / 100)
people = int(input("How many people are splitting the bill? "))
total = bill * percent 
each = round(total / people, 2)

print(f"Each person should pay ${each}")