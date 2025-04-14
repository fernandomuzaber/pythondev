print("Welcome to the tip calculator!\n")

total_bill = float(input("What was the total bill? $"))

tip_percent = float(input("How much tip would you like to give? 10, 12, or 15%?"))

tip_percent /= 100 

people = float(input("How many people to split the bill?"))

result = total_bill *  (tip_percent+1) / people

formatted_result = "{:.2f}".format(result)

print(f"Each person should pay: ${formatted_result }")

