
print("welcom to your budget Tracker platform ")

name =input ("inter your name: ")


while True:
  try:
    budget  = float (input("enter your total monthly budget(AED): "))
    if budget <=0:
      print("❌ Budget must be greater than 0. Please try again.")
    else:   
     break
  except ValueError:
    print("❌ Invalid input.. please enter number only for the budget.")
categories = []
expenses = []
print ("\nplease enter 5 spending categories: ")

for i in range(5) :
    category = input(f"category {i+1}: ")
    categories.append(category)

print("\nEnter How Much You Spent In Each Category:")

for i in range(5):
 while True:
    try:
      amount = float (input(f"{categories[i]}: AED "))
      if amount < 0:
         print("❌ Amount cannot be negative.")
      else:
          expenses.append(amount)
      break 
    except ValueError:
      print("❌  Invalid amount! Please enter a number.")
    

total_spent = sum(expenses)
remining = budget - total_spent

print("\nBudget Summary: ")
print(f"Student Name: {name}")
print(f"Total Budget: AED {budget:.2f}")
print(f"Total spent: AED {total_spent:.2f}")
print(f"Remining Balance: AED {remining:.2f}")



if remining > 0:
    print("☺️  you are within yor budget..Good Job!")
elif remining == 0:
    print("😰  you have used your full budget..warning")
else:
    print("😞  you exceeded your budget..sorry")