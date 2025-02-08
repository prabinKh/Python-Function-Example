# Function to simulate a shopping cart system
def shopping_cart_system():
    cart = {}  # Dictionary to store items and their quantities
    discounts = {
        "DISCOUNT10": 0.10,  # 10% discount
        "DISCOUNT20": 0.20,  # 20% discount
    }
    applied_discount = None

    while True:
        print("\nWelcome to the Shopping Cart System!")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Apply Discount")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        # Add Item
        if choice == "1":
            item = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))

            if item in cart:
                cart[item]["quantity"] += quantity
            else:
                cart[item] = {"price": price, "quantity": quantity}
            print(f"{quantity} x {item} added to the cart.")

        # Remove Item
        elif choice == "2":
            item = input("Enter the item name to remove: ")
            if item in cart:
                quantity = int(input(f"Enter the quantity to remove (current: {cart[item]['quantity']}): "))
                if quantity >= cart[item]["quantity"]:
                    del cart[item]
                    print(f"{item} removed from the cart.")
                else:
                    cart[item]["quantity"] -= quantity
                    print(f"{quantity} x {item} removed from the cart.")
            else:
                print(f"{item} not found in the cart.")

        # Apply Discount
        elif choice == "3":
            discount_code = input("Enter the discount code: ")
            if discount_code in discounts:
                applied_discount = discounts[discount_code]
                print(f"Discount {discount_code} applied successfully.")
            else:
                print("Invalid discount code.")

        # View Cart
        elif choice == "4":
            if not cart:
                print("Your cart is empty.")
            else:
                print("\nYour Cart:")
                for item, details in cart.items():
                    print(f"{item} - ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']:.2f}")
                total = sum(details["price"] * details["quantity"] for details in cart.values())
                if applied_discount:
                    discount_amount = total * applied_discount
                    total -= discount_amount
                    print(f"Discount Applied: -${discount_amount:.2f}")
                print(f"Total: ${total:.2f}")

        # Checkout
        elif choice == "5":
            if not cart:
                print("Your cart is empty. Add items to checkout.")
            else:
                total = sum(details["price"] * details["quantity"] for details in cart.values())
                if applied_discount:
                    discount_amount = total * applied_discount
                    total -= discount_amount
                    print(f"Discount Applied: -${discount_amount:.2f}")
                print(f"Total to Pay: ${total:.2f}")
                print("Thank you for shopping with us!")
                break

        # Exit
        elif choice == "6":
            print("Thank you for using the Shopping Cart System. Goodbye!")
            break

        # Invalid Choice
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    shopping_cart_system()




"""
Global Variables:

cart: A dictionary to store items, their prices, and quantities.

discounts: A dictionary to store discount codes and their values.

applied_discount: Stores the currently applied discount.

Loops:

A while loop for the main menu.

A for loop to iterate through the cart items.

Conditional Logic:

Checks for valid discount codes.

Handles item addition and removal.

Nested Logic:

Calculates the total price and applies discounts.
"""