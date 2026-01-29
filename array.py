expences = [2200,2350,2600,2130,2190,2000]

# 1. In Feb, how many dollars you spent extra compare to Jan?
extra_feb = expences[1] - expences[0]   
print(f"Extra spent in Feb compared to Jan: ${extra_feb}")

# 2. Find out your total expense in first quarter (first three months) of the year.
total_first_quarter = sum(expences[0:3])
print(f"Total expense in first quarter: ${total_first_quarter}")
# 3. Find out if you spent exactly 2000 dollars in any month
exactly_2000 = 2000 in expences
print(f"Spent exactly $2000 in any month: {exactly_2000}")
# 4. Find out the months in which you spent more than 2000 dollars
months_above_2000 = [i+1 for i, expense in enumerate(expences) if expense > 2000]
print(f"Months with expenses above $2000: {months_above_2000}")
# 5. Find the maximum amount you spent in the year
max_expense = max(expences)
print(f"Maximum expense in the year: ${max_expense}")
 