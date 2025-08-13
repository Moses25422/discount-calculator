def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def main():
    try:
        price = float(input("Enter the original price: "))
        discount = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount)
        if discount >= 20:
            print(f"Discounted price: ${final_price:.2f}")
        else:
            print(f"Original price: ${price:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()