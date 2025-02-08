# restaurant management system

"""
1. add dishes to the menu
2. Remove dishes from the menu
3. Takes oreder from the customer
4. Calculate the total bill for an order
5. view all dishes from the menu
6. view all order
7. Calculate the total revenue from the menu

"""
# Global variables to store menu and order data
menu = {}  # Dictionary to store dishes and their prices
orders = {}  # Dictionary to store orders

# Function to add a dish to the menu
def add_dish(dish_id, name, price):
    if dish_id in menu:
        print(f"Dish with ID {dish_id} already exists.")
    else:
        menu[dish_id] = {
            "name": name,
            "price": price
        }
        print(f"Dish {name} with ID {dish_id} added to the menu.")

# Function to remove a dish from the menu
def remove_dish(dish_id):
    if dish_id not in menu:
        print(f"Dish with ID {dish_id} does not exist.")
    else:
        del menu[dish_id]
        print(f"Dish with ID {dish_id} removed from the menu.")

# Function to take an order from a customer
def take_order(order_id, customer_name, dish_ids):
    if order_id in orders:
        print(f"Order with ID {order_id} already exists.")
        return
    order_items = []
    total_price = 0
    for dish_id in dish_ids:
        if dish_id not in menu:
            print(f"Dish with ID {dish_id} does not exist in the menu.")
            return
        order_items.append({
            "dish_id": dish_id,
            "name": menu[dish_id]["name"],
            "price": menu[dish_id]["price"]
        })
        total_price += menu[dish_id]["price"]
    orders[order_id] = {
        "customer_name": customer_name,
        "items": order_items,
        "total_price": total_price,
        "status": "Pending"
    }
    print(f"Order {order_id} taken for {customer_name} with total price ${total_price:.2f}.")

# Function to calculate the total bill for an order
def calculate_bill(order_id):
    if order_id not in orders:
        print(f"Order with ID {order_id} does not exist.")
        return
    total_price = orders[order_id]["total_price"]
    print(f"Total bill for order {order_id}: ${total_price:.2f}")

# Function to view all dishes in the menu
def view_menu():
    if not menu:
        print("The menu is empty.")
    else:
        print("\nMenu:")
        for dish_id, dish in menu.items():
            print(f"Dish ID: {dish_id}, Name: {dish['name']}, Price: ${dish['price']:.2f}")

# Function to view all orders
def view_orders():
    if not orders:
        print("No orders have been placed.")
    else:
        print("\nAll Orders:")
        for order_id, order in orders.items():
            print(f"Order ID: {order_id}, Customer: {order['customer_name']}, Total Price: ${order['total_price']:.2f}, Status: {order['status']}")
            print("Items:")
            for item in order["items"]:
                print(f"  Dish ID: {item['dish_id']}, Name: {item['name']}, Price: ${item['price']:.2f}")

# Function to calculate the total revenue from all orders
def calculate_total_revenue():
    total_revenue = sum(order["total_price"] for order in orders.values())
    print(f"Total revenue from all orders: ${total_revenue:.2f}")

# Main function to interact with the user
def __main__():
    while True:
        print("\nWelcome to the Restaurant Management System!")
        print("1. Add Dish")
        print("2. Remove Dish")
        print("3. Take Order")
        print("4. Calculate Bill")
        print("5. View Menu")
        print("6. View Orders")
        print("7. Calculate Total Revenue")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            dish_id = input("Enter dish ID: ")
            name = input("Enter dish name: ")
            price = float(input("Enter dish price: "))
            add_dish(dish_id, name, price)

        elif choice == "2":
            dish_id = input("Enter dish ID to remove: ")
            remove_dish(dish_id)

        elif choice == "3":
            order_id = input("Enter order ID: ")
            customer_name = input("Enter customer name: ")
            dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
            take_order(order_id, customer_name, dish_ids)

        elif choice == "4":
            order_id = input("Enter order ID to calculate bill: ")
            calculate_bill(order_id)

        elif choice == "5":
            view_menu()

        elif choice == "6":
            view_orders()

        elif choice == "7":
            calculate_total_revenue()

        elif choice == "8":
            print("Thank you for using the Restaurant Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    __main__()

