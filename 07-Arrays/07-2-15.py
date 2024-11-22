
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr


car_fuel_consumption = [12.5, 8.2, 15.6, 10.3, 7.9] 
print("Original car fuel consumption:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)


bank_transactions = [350.75, 22.50, 1180.40, 500.00, 950.00]
print("Original bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)
