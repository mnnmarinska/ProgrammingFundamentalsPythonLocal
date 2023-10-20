total_price_without_taxes = 0
customer_type = ""

while True:
    command = input()
    if command == "special" or command == "regular":
        customer_type = command
        break
    else:
        command = float(command)
        if command <= 0:
            print("Invalid price!")
            continue
        taxes = command * 0.20
        total_price_without_taxes += command

if total_price_without_taxes == 0:
    print("Invalid order!")
else:
    total_amount_of_taxes = total_price_without_taxes * 0.20
    total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes

    if customer_type == "special":
        total_price_with_taxes *= 0.90

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")