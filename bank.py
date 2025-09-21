credit_score=float(input("Enter the credit score"))
annual_income=float(input("enter the annual income"))
debt_to_income_ratio=float("enter debt-to-income ratio")

while True:
    if credit_score<=650:
        print("not elligible")
        break
    else:
        print("good credit score")

    if annual_income<=3000:
        print("not elligble")
        break
    else:
        print("income approved")

    if debt_to_income_ratio<=0.4:
        print()
    