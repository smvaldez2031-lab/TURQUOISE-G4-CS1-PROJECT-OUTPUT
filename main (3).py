def Compute(allowance, saved, exp_1, exp_2, exp_3, time):
    budget = allowance / time
    total = budget + saved
    spent = exp_1 + exp_2 + exp_3
    savings = total - spent
    return savings
def Display(savings, days):
    if savings < 0:
        warn = (savings*-1)
        per_day = warn / days
        print(f"WARNING!, You have spent more than your budget by {warn:.2f} peso(s)!")
        print(f"Spend {per_day:.2f} peso(s) less per day to stay within your budget.")
    elif savings == 0:
        print("Caution, you have spent the same amount as your budget.")
    else:
        per_day_save = savings / days
        print(f"You have saved {savings:.2f} peso(s).")
        print(f"You saved around {per_day_save:.2f} peso(s) saved per day.")
name_1 = input("Please Enter your first name: ")
while name_1 == "":
    name_1 = input("Please Enter your first name: ")
name_2 = input("Please Enter your last name: ")
while name_2 == "":
    name_2 = input("Please Enter your last name: ")
print("Hello,", name_1, name_2)
time = int(input("Please enter (1) if your budget is weekly, or (2) if it is monthly: "))
while time == "":
    time = int(input("Please enter (1) if your budget is weekly, or (2) if it is monthly: "))
if time<=0 or time >= 3:
    print("INVALID INPUT")
    quit()
allowance = int(input("Enter your allowance: "))
saved = int(input("Please Enter how much you saved on your budget: "))
expense_1 = int(input("Please Enter how much you spent on transportation: "))
expense_2 = int(input(" Please Enter how much you spent on consumables: "))
expense_3 = int(input("Please Enter how much you spent on other expenses: "))
if time == 1:
    savings = Compute(allowance, saved, expense_1, expense_2, expense_3, 7)
    Display(savings, time)
else:
    savings = Compute(allowance, saved, expense_1, expense_2, expense_3, 31)
    Display(savings)
