price=float(input())
discount=float(input())*0.01
price_with_discount=round(price-price*discount , 2)
reduction=round(price-price_with_discount , 2)
print(f"price_with_discount:{price_with_discount} Reduction {reduction}")