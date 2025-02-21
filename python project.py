warehouse = {}

# Function to insert a new warehouse record
def insert_warehouse():
    product_id = input("Enter product ID: ")
    if product_id in warehouse:
        print("Product already exists!")
    else:
        product_name = input("Enter product name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))
        location = input("Enter location: ")
        warehouse[product_id] = {"product_name": product_name, "category": category, "quantity": quantity, "location": location}
        print("Warehouse record added successfully!")

# Function to update warehouse details
def update_warehouse():
    product_id = input("Enter the product ID to update: ")
    if product_id not in warehouse:
        print("Product does not exist!")
    else:
        print("Choose what to update:")
        print("1: Product Name")
        print("2: Category")
        print("3: Quantity")
        print("4: Location")
        print("5: Update All")
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1 or choice == 5:
            product_name = input("Enter new product name: ")
            warehouse[product_id]["product_name"] = product_name
        if choice == 2 or choice == 5:
            category = input("Enter new category: ")
            warehouse[product_id]["category"] = category
        if choice == 3 or choice == 5:
            quantity = int(input("Enter new quantity: "))
            warehouse[product_id]["quantity"] = quantity
        if choice == 4 or choice == 5:
            location = input("Enter new location: ")
            warehouse[product_id]["location"] = location
        
        print("Warehouse record updated successfully!")

# Function to display all warehouse records
def display_warehouse():
    if not warehouse:
        print("No products in the warehouse.")
    else:
        print("\nWarehouse Records:")
        for product_id, details in warehouse.items():
            print(f"ID: {product_id}, Name: {details['product_name']}, Category: {details['category']}, Quantity: {details['quantity']}, Location: {details['location']}")

# Function to delete a warehouse record
def delete_warehouse():
    product_id = input("Enter the product ID to delete: ")
    if product_id not in warehouse:
        print("Product does not exist!")
    else:
        del warehouse[product_id]
        print("Warehouse record deleted successfully!")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nChoose an action:")
        print("1: Create")
        print("2: Update")
        print("3: Delete")
        print("4: Display")
        print("5: Exit")
        
        try:
            action = int(input("Enter your choice (1-5): "))
            if action == 1:
                insert_warehouse()
            elif action == 2:
                update_warehouse()
            elif action == 3:
                delete_warehouse()
            elif action == 4:
                display_warehouse()
            elif action == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")