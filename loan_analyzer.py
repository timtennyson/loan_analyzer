# coding: utf-8
import csv
from pathlib import Path

#------------------------Part 1: Automate the Calculations.--------------



#The following are loan costs to be used in the calculations below:
loan_costs = [500, 600, 200, 1000, 450]

#Calculates the total number of loans in the list:
number_of_loans = len(loan_costs)
print(f"the total number of loans is {number_of_loans}")

#Calculates the sum of all loans:
total_amount = sum(loan_costs)
print(f"the total amount is: {total_amount}")

#Calculates the average loan amount:
average_loan_price = str(total_amount / number_of_loans)
print (f"the average_loan_price is: {average_loan_price}")


#-----------------------Part 2: Analyze Loan Data.---------------------------


#Analyze the loan to determine the investment evaluation.
#Loan data:
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract the Future Value and Remaining Months on the loan above.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Print each variable.
print(f"the future value of the loan is: {future_value}")
print(f"the number of months remaining is: {remaining_months}")


# Calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
# Use the **monthly** version of the present value formula.
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate = 0.20
present_value = future_value / (1+ discount_rate/12) ** remaining_months

# Conditional statement to decide if the present value represents the loan's fair value.
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price")

#test to make sure the value between the original loan and the new loan below are different-- comment out
#print(present_value)


#---------------------Part 3: Perform Financial Calculations.------------------------------


#perform financial calculations using functions.
#calculate the present value for the loan below.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Define a new function for present value
def fair_value():
    future_value = new_loan.get("future_value")
    remaining_months = new_loan.get("remaining_months")
    present_value = (future_value / (1+ discount_rate/12) ** remaining_months)
    return present_value
    
# Calculate the present value of the new loan
# "annual_discount_rate" of 0.2 for this new loan calculation.
# print the present value
discount_rate = 0.2
print(f"the present value of this loan is: {fair_value():.2f}")

#Here is a list of loan data for calculations below:
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(f"this is the list of inexpensive loans:{inexpensive_loans}")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
        



