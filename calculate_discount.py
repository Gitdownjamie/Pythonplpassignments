# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# Main program
try:
    # Prompt user for inputs
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Call function
    final_price = calculate_discount(original_price, discount)

    # Print result
    if discount >= 20:
        print(
            f"Final price after applying {discount}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")

# Enter the original price of the item: 1500
# Enter the discount percentage: 15
# No discount applied. The price remains: 1500.00


# Enter the original price of the item: 1500
# Enter the discount percentage: 30
# Final price after applying 30.0% discount is: 1050.00
