###
# Sums numbers entered by user
#
total_sum = 0
i=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    i=i+1
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    average=total_sum/i



print(f"The total sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")