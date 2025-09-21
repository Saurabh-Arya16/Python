#Program to find appropriate discounts
mobile_price = float(input("Enter the price of the mobile:"))
choice = input("Are you buying a powerbank with the mobile? (yes/no): ").strip().lower()

if choice == 'yes':
    powerbank_price = float(input("Enter the price of the powerbank:"))
    mobile_discount = mobile_price * 0.25
    discounted_mobile_price = mobile_price - mobile_discount
    total_price = discounted_mobile_price + powerbank_price
else:
    mobile_discount = mobile_price * 0.05
    total_price = mobile_price - mobile_discount
print(f"Total price: {total_price:.2f}")