
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]


max_expense_index = expenses.index(max(expenses))


most_expensive_category = categories[max_expense_index]
most_expensive_amount = expenses[max_expense_index]


print(f"The most expensive category is '{most_expensive_category}' with an expense of {most_expensive_amount}.")
